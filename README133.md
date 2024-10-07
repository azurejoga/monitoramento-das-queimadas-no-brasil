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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c47293ab-596b-385c-adec-c486def71562 | -10.51743 | -68.40276 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08803b7e-3c78-36a8-9bcb-67435e1b45b1 | -10.53066 | -68.03954 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b58552a0-9e19-3a32-9a76-cfedd357ada7 | -10.53126 | -68.0358 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76041080-1081-35b6-adb4-bff8b3c099c7 | -10.54672 | -68.02688 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da48f399-4293-39e6-8cbe-bb09259d0fa3 | -10.55073 | -68.02372 | 2024-10-07 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34193fa9-bfe0-3461-8ba6-c342096a78cc | -9.62899 | -67.47774 | 2024-10-07 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11a07c84-949e-31e8-a378-51c0ae700bb0 | -9.63236 | -67.47829 | 2024-10-07 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e757d9-a780-3786-9ea4-10e569283b9b | -9.49397 | -67.11514 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adbba90d-597e-342d-beaa-c1cad6405439 | -9.49454 | -67.11156 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68700fc0-97c4-3fde-a7a9-3774f20832da | -9.58835 | -66.75903 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eecc339-2991-330d-861b-12e48c4e32a6 | -9.58891 | -66.7555 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5313e040-e1f7-37a1-857f-98f7f1087490 | -9.58947 | -66.75198 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd5342b8-795d-3fab-855b-174d670b1af7 | -9.59224 | -66.75604 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6daea873-c7d8-3828-8370-3a23a2a50687 | -9.5928 | -66.75251 | 2024-10-07 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93b135ac-fa67-3b97-869e-6f68355bc11b | -9.74043 | -66.33414 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ec10eb3-af97-3a3f-99a7-4becad19259b | -9.87745 | -66.79868 | 2024-10-07 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b17f183-262e-3a2d-acdb-67ca82398f84 | -9.87801 | -66.79516 | 2024-10-07 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc236acb-be53-346f-a293-ff3726193f02 | -9.97973 | -66.75411 | 2024-10-07 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e2032a2-7c08-3a95-be2d-43e835057254 | -9.73898 | -63.99244 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a2736c-c881-3cdc-869d-7beea65accb3 | -9.73841 | -63.99619 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6727eb60-e8a2-3aee-b829-924070c9a387 | -9.61411 | -64.05406 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a671fd3-9ed5-3c58-8e75-86edcfcf8868 | -10.64153 | -64.52751 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7845154-db95-3abe-9f15-78ea33f50c16 | -10.64097 | -64.53121 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fde4db38-4930-322a-888c-75d174cad374 | -10.63758 | -64.53069 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae99cdb4-554a-398b-a911-88c22128c87d | -10.63018 | -64.51072 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad9c750-37c5-33de-b70d-86345b7b287f | -10.62961 | -64.51447 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27ca104c-136c-3b0d-894c-c56ae9b869ac | -10.62807 | -64.36266 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2f8dc5b-3a58-34f2-b8b6-712d047807fd | -10.61841 | -64.35727 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 700c7f2c-3418-3f51-82fe-4dff3993595f | -10.61811 | -64.3577 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53928fdf-3399-352a-b856-f9b33a6ad4ea | -10.59311 | -64.4072 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 607effb2-909b-3dc8-b04e-56d61f675801 | -10.5897 | -64.4067 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b6cf17-2ebc-3822-9102-a106409e208b | -10.58914 | -64.41039 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd39a59e-3b47-3ee6-a915-1c6cfbb85661 | -10.58858 | -64.41405 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d6d931e-3ff5-3ed1-9e24-a696270d7c9b | -10.34218 | -64.2626 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68b59f43-d1a0-3773-ab0f-7ac555d43170 | -10.33933 | -64.25834 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2e41bb8-200a-3349-8704-f2ad16e0a226 | -10.33876 | -64.26208 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c79ccafc-890d-3e50-8e44-f3988e81dca6 | -10.33591 | -64.25782 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf809ee-573b-3a0e-836c-da83d156a23c | -10.33535 | -64.26157 | 2024-10-07 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4658b5c-94da-3f48-b511-56351f88c877 | -9.44039 | -63.62471 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a08e550d-97be-3e9a-afed-88be3bacaf18 | -9.43982 | -63.62856 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b93f98-537f-3d98-8ee3-d24233dff6dc | -9.43692 | -63.62415 | 2024-10-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9033ad7f-fdf2-39b2-82cd-cb1092bb5465 | -9.43635 | -63.62801 | 2024-10-07 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ebc1d9c-6ca6-3847-b46a-8b1cc8b9064d | -10.69537 | -63.46793 | 2024-10-07 05:42:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d50d71-9867-3cca-8415-5c0157864732 | -10.59971 | -63.74184 | 2024-10-07 05:42:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f8e0ed-4874-333a-9174-15de372cf5f4 | -10.59912 | -63.74573 | 2024-10-07 05:42:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8753317b-ebac-3bfb-b409-24060d790ea5 | -10.59622 | -63.7413 | 2024-10-07 05:42:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e371a18b-fa7f-3b61-b891-943b42fbf049 | -10.97631 | -63.97979 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b60fc13-819c-310a-aefe-cfe9dcf8fe5e | -10.9021 | -64.19176 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 853c4679-47bc-3849-8b39-58507910d99b | -10.88769 | -64.1705 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18fa1f5e-4281-3fc3-aebf-e7cff472a3c1 | -10.84525 | -64.17651 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72eca235-1b77-3703-87b2-80a7dfd4c5f2 | -10.84242 | -64.17204 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b878858-99b9-34d1-863f-a91d2673ba5e | -10.99258 | -63.91896 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ca236f9-901d-3dae-a73e-8bcf7f838e3a | -10.92243 | -63.88849 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3e1fdf9-f681-32e0-a36b-6ed8bec3cf2d | -10.91837 | -63.8919 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71020692-ac8c-3ca1-9544-c471311ba384 | -10.91475 | -63.86824 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a21274-e283-34a6-9248-d1d3403fe4ae | -10.91432 | -63.89527 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb43108c-ead9-3587-a9f1-e9bfd43f1982 | -10.91182 | -63.86399 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 667eb0fb-e507-3357-b148-b91c4bdebab8 | -10.90206 | -63.89481 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6e8256-8333-309d-97e7-3cf588c69d6a | -10.90097 | -63.91357 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1016bfc4-c104-39b2-9a49-3237c238f8b7 | -10.88925 | -63.90901 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c162b56a-b64f-3b93-9005-715df1aa9052 | -10.88868 | -63.91278 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07b55564-a26d-39c8-890f-3bee2b1d2686 | -10.88578 | -63.90847 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d1e39a-d0c5-381b-b64f-486f14001f68 | -10.88521 | -63.91227 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb35dfdf-6597-3658-9d2f-281f0891382b | -10.8829 | -63.90401 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c486eec-3426-3bfc-9f63-8116cea3233f | -10.88232 | -63.90787 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e77948-45e4-3e87-9a03-4a7a1e4b4fe6 | -10.88004 | -63.89941 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e063111-c907-3073-9b8c-110086da66f7 | -10.87945 | -63.90332 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86b7a126-ac9e-3649-ba93-9dd7f6c9f061 | -10.87886 | -63.90725 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40d733f0-345d-383a-bf47-085f2df9a725 | -10.87767 | -63.91512 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abb4993a-ca58-3c2d-bbaf-6071f3b16d31 | -10.87716 | -63.89491 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689fcc90-5bb9-3add-896d-11794366fdd2 | -10.87709 | -63.91901 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97c0f2cc-a8fc-3b7f-976e-8e7a0923f29f | -10.87658 | -63.8988 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97ef559e-288c-344c-a114-ecfdd7faf30a | -10.87651 | -63.92286 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d3743bf-de09-39fe-8155-a29fda555307 | -10.87599 | -63.9027 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d62ae930-fda2-3c0f-af8c-c0204ff4d802 | -10.87479 | -63.91066 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e4c81b9-a1c0-3fcf-bc93-f3c436c2649f | -10.8742 | -63.9146 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7589414-6138-3474-a2f4-cf8eb6f462b2 | -10.8737 | -63.89433 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8e6066b-54da-3cb4-bd8e-571c3311f034 | -10.87361 | -63.91848 | 2024-10-07 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f2dbc4c-1794-344c-9637-3fd66f78fdf6 | -19.10687 | -57.5144 | 2024-10-07 05:44:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8a476bbd-c2e6-3af3-98c7-f09864949f2c | -19.10589 | -57.51132 | 2024-10-07 05:44:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cd520803-7324-3de0-ac19-dca5db3d2d22 | -19.10553 | -57.51486 | 2024-10-07 05:44:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b0a4fff2-78a6-3d39-a9eb-f85a798b578b | -18.72863 | -57.29304 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3eee73a7-f403-38cc-bd5a-4966fa98c9c0 | -18.72822 | -57.2973 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3f584889-b292-33a2-976c-235478871453 | -18.72807 | -57.29591 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f1005e44-5b5f-3343-ab1a-9c404ac5e5ff | -18.72781 | -57.30154 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1344678e-bb11-3ea5-a5f5-cccaa0dbee5d | -18.72763 | -57.30014 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4dcd3fb0-8f8d-3386-b145-6c9f8adc5fe4 | -18.72324 | -57.28814 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6590306a-cc24-32ca-a092-bf512f055dd0 | -18.72282 | -57.29242 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 274d1d7a-40cc-300a-bf36-bcf0dc792036 | -18.7227 | -57.29105 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9e24b3d-e648-3e30-90a4-ac1e66c71364 | -18.72241 | -57.29667 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2c61ce1b-dbe3-3ee9-abdd-15409fd59bf5 | -18.72226 | -57.2953 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6ba3529d-98f3-30bc-ba6e-9a6db6bce49e | -18.722 | -57.30091 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9d5ec7df-75ea-3235-9593-87d9862b2e18 | -18.72182 | -57.29954 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b2f68ce2-ce73-3866-bea4-7239935fe3a6 | -18.72159 | -57.30516 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| ada5c91d-3323-3b5b-bee7-526c41fb0be0 | -18.72138 | -57.30377 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 18e4e663-3e41-3a7a-acbc-f814c9149f44 | -18.72094 | -57.30802 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 56b76e54-1a57-3807-8e0c-fd18178b86df | -18.71742 | -57.28751 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 493c75f1-92df-3caa-81d5-6806e6b51882 | -18.71701 | -57.29177 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 41ce9952-a2d0-300f-83cd-0855f9311153 | -17.1592 | -57.34453 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| cf8afb35-5b3c-3bb7-a11c-2315c8f1e89c | -17.15878 | -57.34854 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |


[Clique aqui para ver as próximas entradas](README134.md)
