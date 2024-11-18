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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba26c94d-15ea-3691-a6a0-0df9a746a4f3 | -2.92969 | -46.73041 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62d776e4-4058-3fb1-a85c-53772eb1ed99 | -2.29686 | -46.44328 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99cbd2d0-45b4-35ff-8c22-ce7f6adb4b80 | -2.67993 | -46.22802 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98d33619-ac0e-310c-9547-33de49886e10 | -2.63097 | -46.56187 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7efcabab-a198-3e7e-a467-690ba47935de | -1.29952 | -51.73597 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 655ebf1d-a3fc-34b8-99b4-9a5028323562 | -2.6363 | -46.52822 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2319f7e-7421-3bfd-9b6d-d72e292b231e | -1.29891 | -51.73967 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 57c4c17a-eb42-36a5-9636-60f709b2c77d | -2.95245 | -48.00402 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd1b2edd-683c-37cb-9db0-93e08eef681d | -3.33121 | -46.01262 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a7122d4-9d93-350b-b110-1811b55151d4 | -2.4264 | -46.53399 | 2024-11-18 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47848b86-d900-3aa7-ba8e-9da166ef71ab | -2.17185 | -50.61193 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4e2a3b-8c29-3735-9bad-cea5727d23ad | -2.95631 | -48.00772 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 119d47bb-9a7f-3558-ad24-390854ed32c1 | -1.62093 | -53.30351 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 780c157c-7907-3215-9b0b-a4f4ce6986c8 | -3.57227 | -45.21189 | 2024-11-18 04:10:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e81e646e-4bc1-3c6b-a81c-f1065f94a620 | -0.89202 | -52.7276 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8befc67d-8a00-3766-8113-ee5df70f9d06 | -2.94399 | -48.32063 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f8526ff-eb1f-3b6e-8823-27c3e73e88ee | -2.42659 | -48.64111 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b048aab3-e681-3be9-a1c2-6992846d985c | -2.76382 | -52.61346 | 2024-11-18 04:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d150ca6a-84f2-3342-8071-d5502fe8ec36 | -1.2983 | -51.74337 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| ba6534c2-165c-3308-aeec-86b95c770e24 | -3.22756 | -42.97863 | 2024-11-18 04:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca7bd518-0031-3875-8c01-c17447ff7e35 | -2.65102 | -46.56009 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 700e5760-5b43-311e-a1b1-8398667d711b | -2.85231 | -46.66815 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90c8e72b-217a-3946-adc8-d5c6c97cd857 | -3.23017 | -49.12804 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274694e3-36db-3460-9e6b-41e8159fc9d4 | -2.8845 | -42.74076 | 2024-11-18 04:10:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f186029-57e2-38fc-b808-087cfcc7a246 | 0.61327 | -51.77462 | 2024-11-18 04:10:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71c8723b-72ab-3db0-b39f-b4b4a9547217 | -3.23471 | -49.12872 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97976d00-e425-3a3a-9b9a-17f01411eb3d | -2.18569 | -50.33611 | 2024-11-18 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b00ca64-5965-3a79-abee-23914d42cdb4 | -2.19594 | -53.66657 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fcf25306-2cf8-3ff3-aa0b-75374f75b9c0 | -2.90711 | -46.84738 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ac859f7-8ea1-3dc6-90ce-2fe8d75b3ec7 | -3.04475 | -49.56369 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdcb6c1-8217-3c7f-b04a-5212360da835 | -2.90792 | -46.84229 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0310472-bbb2-3702-b4ec-0dc18ab21451 | -2.67761 | -46.21824 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f6a2bc1-4110-3d8a-8e73-5235438b82f8 | -2.3354 | -49.13739 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db0bd0a9-997f-3017-9335-6dfb440f640a | -1.15629 | -49.11494 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ffc0be6-b0fe-3ed8-850f-09c16381681b | -3.1869 | -45.44394 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4e69b4a-dd63-38c0-8107-58c518a27223 | -1.29272 | -51.74247 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d503b12a-d99b-304f-9af3-9f3d39e1d1f7 | -2.92906 | -48.33077 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f46e734-509b-3ad4-b79d-5dc226cb8740 | -2.23042 | -53.61261 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8c4b9dc-1be8-3a1a-bbf5-ff3e51685003 | -5.07037 | -37.71713 | 2024-11-18 04:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee4c742e-90d5-32fc-81f0-5fac0e7f8bab | -2.84421 | -46.66008 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b5174c2-f4c3-3072-987a-d29f2e618a3b | -1.20697 | -51.78686 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c230ba07-81ac-3766-b0cc-0b6a4bd5aba6 | -3.06047 | -48.00498 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 916f4c6f-f663-3b0e-9925-d8abdd2435e0 | -2.64286 | -46.84188 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ad0ee8a-51b9-3eba-818b-32f682a2cf81 | -1.36972 | -47.26129 | 2024-11-18 04:10:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f6e12d0-7420-31b7-b84d-bf5e09d47733 | -2.77826 | -51.75661 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe03eef-3c1a-3baf-82ab-572ad92a9aad | -1.70396 | -45.8367 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 35aa2585-746e-3c36-94e8-d638e640a97c | -2.96052 | -48.00844 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b5de596-d375-3ae4-91eb-cbf4614faed6 | -3.08564 | -49.20601 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba31c6aa-545d-3e62-bfc8-9c2d60873371 | -3.37617 | -46.50423 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db783bf1-6d85-3d21-82e6-ecffb619cb2e | -2.92261 | -48.0553 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa227786-e67e-3ce5-ac0a-51317be3a08d | 0.17279 | -51.2705 | 2024-11-18 04:10:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6009ee1-07a2-395f-a850-306b05b85f5f | -2.68443 | -46.22405 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc2be7f4-1cf3-34ec-be65-5423c486fdfe | -2.69597 | -49.28828 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7628c6f9-ddd1-371b-a7c8-6316f7739060 | -3.17287 | -46.44268 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f5026b4-d133-38da-893f-fef1d89a779e | -2.22386 | -46.46815 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52a7fe4f-8a44-383b-b996-3fe04c5979b9 | -1.29211 | -51.74617 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3338123-d253-307a-a16c-e4620b5cef0a | -1.37032 | -47.25762 | 2024-11-18 04:10:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bae0cc38-aee1-34aa-81c3-54f35989f22a | -2.71767 | -51.81278 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef1c098-20be-367c-81e2-4454b3301af3 | -2.84345 | -46.66491 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5be81d32-3af1-3ec8-a57d-dc8bb655976d | 0.61966 | -51.77768 | 2024-11-18 04:10:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1d1275b2-fcea-3fd5-a2af-39f3879e4a52 | -3.32751 | -46.01197 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40e50f58-022b-3ea7-9126-72758172d0b5 | -3.04394 | -49.56857 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f465a757-9849-3192-8c20-7a391ebc6d04 | -3.18397 | -45.43925 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3b216a8-1c82-3fae-8de3-286b98a6c1ed | -1.70468 | -45.8322 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 304f7106-7d54-3161-9d9c-a1b9c05db453 | -2.57936 | -51.7268 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 675e1093-2592-3675-bac1-97f9c94a9b21 | -2.57876 | -51.73034 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f93b7e2-003a-3330-a358-f58a3d1fda4c | -2.91022 | -46.85308 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 050c8e9e-462a-3409-9e63-8610a587c952 | -1.61779 | -52.62881 | 2024-11-18 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94ee7e15-f273-3fc7-9f38-b8726876469e | -3.27796 | -46.1766 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121e05f7-da35-3842-ac34-852cc8198e76 | -2.29861 | -49.13129 | 2024-11-18 04:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af2e874f-ccb0-3141-840d-32324efed6f8 | -1.89314 | -46.45296 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8c4514-53b7-39e0-a2b3-213ee3f0cd76 | 0.97701 | -51.13998 | 2024-11-18 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0921264-48ce-3ba4-8060-2da1bc180d50 | -2.93828 | -48.06594 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cc40c7c8-2105-34b0-949e-901d4f8849dc | -1.43154 | -53.38889 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6e40752-f02e-3f14-abf1-cdff903f8d7e | -2.07925 | -46.47217 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2150ae96-9eed-3b1d-a3c3-4f0942bb1585 | -2.10998 | -46.42796 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f617d3f-f0bc-31c0-91ef-2508d511a5e4 | -2.71962 | -48.34094 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3891edde-bc87-3dca-b41a-3f920f4520bd | -2.54854 | -47.29581 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51157c1-7525-374e-80ff-362cbce3c8ac | -2.94897 | -48.31724 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8a7b487-2455-3ded-804c-17b3a34492f7 | -2.33988 | -49.13528 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e63515f-e003-37a5-892b-af9816833d12 | -2.63504 | -46.84044 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5486330c-c983-37aa-a63b-ae244a45c85c | -1.81242 | -46.53496 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1ce4293a-8ef5-325a-8ddb-a77bea783cbf | -0.94976 | -51.7299 | 2024-11-18 04:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a27acf9-ffd5-3f71-82be-cea21d837f0c | -2.65277 | -46.22832 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 915d0984-26eb-37c9-a8ed-0859efab3454 | -2.18068 | -50.33529 | 2024-11-18 04:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a26513-b3a7-3b19-b4a0-e0ee94141ed9 | -2.75145 | -49.32704 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e29732-3ec7-3fb4-8b77-42fd0fe1caa1 | -2.66861 | -46.22616 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cdd1c8c-6595-390f-963a-66ba3a982f8e | -2.40642 | -48.60395 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93822740-95cb-38af-ade0-3b3c517d374b | -2.61644 | -46.18955 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76f5fb3a-feee-34a4-b876-8fa6295edb78 | -3.94262 | -44.10236 | 2024-11-18 04:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40d4a17e-3916-3ed8-aa51-5e77991abefc | -3.2817 | -46.17718 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92f3c2e1-d48e-385c-b299-29d3b7b83224 | -2.86323 | -51.78582 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5fd7cc9-c6ff-30fb-8d8d-de132b68a35d | -3.30238 | -45.67924 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7cd24e5f-7fb0-30af-9c67-1c12d3bf5e8b | -1.70541 | -45.82771 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 507232f9-784d-3459-9247-04feeab079b9 | -0.95537 | -51.73082 | 2024-11-18 04:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c378441-e816-356f-9f47-0f312e38c36b | 0.97643 | -51.13632 | 2024-11-18 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80c28c6e-e9aa-3eae-a208-2c9159dc3c49 | -1.29333 | -51.73877 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a5d9371-d2d6-3c0d-b2b0-838f740f7606 | -2.57449 | -51.72233 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd201f4d-9a14-3ecf-bc4e-01d11a9e35c3 | -2.28143 | -53.64088 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07c32b45-c512-3b7a-aff5-bbc406675948 | -2.18546 | -46.58593 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
