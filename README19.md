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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abb25702-8121-3950-8d02-e1be542e6c4b | -3.4565 | -50.3622 | 2024-11-07 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 47a142be-3258-3125-90ef-9d4133f2cb8c | -2.82 | -52.9613 | 2024-11-07 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3fdc4073-1206-389b-aff2-05447c1bbef7 | -4.522 | -42.8608 | 2024-11-07 01:40:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a098a5d2-cc66-37b0-9045-6fa13b7c08c1 | -2.6228 | -51.3038 | 2024-11-07 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 287807b2-7fcc-3c7b-b70c-c60095f6f550 | -3.4564 | -50.3832 | 2024-11-07 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fdecdc49-ce55-3f4f-b021-0ed2cd5178f7 | -2.6229 | -51.2831 | 2024-11-07 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 77452f05-3bbf-3c9f-be09-21954bbea133 | -2.924 | -49.5994 | 2024-11-07 01:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 66c8878e-f080-3246-9243-7d4ee58b94fa | -5.1395 | -47.7008 | 2024-11-07 01:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fe5d4c61-181b-31a2-8e6b-8d496931113e | -2.6045 | -51.2835 | 2024-11-07 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d41bf144-d8ac-3230-8b31-2d72268e635c | -5.1581 | -47.6997 | 2024-11-07 01:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 30b23b0d-afcc-3390-8a0a-9ad1238008ac | -4.5031 | -42.8854 | 2024-11-07 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 85405507-c9e7-35f4-aac7-0a69a9ec1be5 | -5.9975 | -45.3607 | 2024-11-07 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e729b82a-1503-333f-8baa-f1c773ae6eba | -3.9669 | -48.1716 | 2024-11-07 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| afe775b9-06e0-3a68-a49a-2008e0f26794 | -1.1831 | -53.8985 | 2024-11-07 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ce8798e0-d87b-39c3-b6bd-94b9fba8fbf1 | -1.2014 | -53.8983 | 2024-11-07 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 80b4e20c-370a-3cd8-a253-20cd7d5c0afd | -3.7033 | -48.9986 | 2024-11-07 01:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6f57ad86-0b30-3568-8308-edb41d04ebc2 | -2.6229 | -51.2831 | 2024-11-07 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3b9f0cce-089e-33a1-9620-2808dce30e40 | -11.8442 | -43.891 | 2024-11-07 01:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2f054a39-7fa1-325f-b586-005998a08fcf | -3.1617 | -50.2038 | 2024-11-07 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0051e6fe-8ffb-3e2c-8249-604a671a675c | -1.1831 | -53.8985 | 2024-11-07 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f3725501-bd5a-3ad1-b8b8-5c456161a0ae | -2.82 | -52.9613 | 2024-11-07 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| eee5396e-a534-32dc-9d4a-05e44c561726 | -4.5218 | -42.8843 | 2024-11-07 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 73ec2fc2-5c11-3039-9fd0-17b00214ba90 | -3.967 | -48.15 | 2024-11-07 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e4b603d7-6ace-336d-b5aa-2cbdebc0d90b | -4.5033 | -42.862 | 2024-11-07 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4e6b285f-7790-3710-9928-b52343f89c5a | -2.8537 | -48.6642 | 2024-11-07 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| cdd32d98-1748-3eb1-8de0-fa825c8f9bf2 | -2.8352 | -48.6648 | 2024-11-07 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 0c640493-4197-3898-b40d-429e91d11940 | -4.522 | -42.8608 | 2024-11-07 01:50:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 72c9da07-ac63-3d07-9e6e-2f0005b127b3 | -2.8536 | -48.6856 | 2024-11-07 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 47104b12-f26f-33aa-b26e-d8227afa3e03 | -1.2014 | -53.8983 | 2024-11-07 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 787bc0c9-3c5c-3ab2-95a2-31e891a75f55 | -2.5009 | -49.1015 | 2024-11-07 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a354c355-2a5e-3c93-abf3-484ea8d7bdc0 | -2.924 | -49.5994 | 2024-11-07 01:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8b83ac91-7d39-385b-8a8c-a80741614f22 | -5.1395 | -47.7008 | 2024-11-07 01:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6f046d0d-5888-3887-9a97-5392bd3c13d7 | -2.5009 | -49.1228 | 2024-11-07 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ce6f8b6a-8e2e-3a76-8e96-92e0d691f9d0 | -3.0396 | -53.2805 | 2024-11-07 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ea2574d4-06ec-320f-add8-52158b2f454b | -2.6228 | -51.3038 | 2024-11-07 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| e35f19d3-8331-32ce-a6f9-8a21a6d53902 | -3.9669 | -48.1716 | 2024-11-07 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9cba32b9-6860-3148-ba6b-bdec9e048d06 | -5.1581 | -47.6997 | 2024-11-07 01:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4fcf8b49-5eb0-316a-ae20-e8972b59fc2a | -3.0207 | -53.443 | 2024-11-07 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d27b4df9-fd85-36d1-9d1f-772b33bbcda6 | -5.9788 | -45.3621 | 2024-11-07 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 66c3a9c5-9b39-3fb3-97bd-1392a0d834f1 | -11.8639 | -43.8644 | 2024-11-07 01:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1df556c8-0b7b-3716-90d2-83a070fa11ac | -1.1466 | -53.7177 | 2024-11-07 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0dbb8827-0237-30e9-b9e9-2dc7045ea147 | -2.82 | -52.9409 | 2024-11-07 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 5e8b7f67-fecb-39f9-b8df-40587095efd9 | -11.8446 | -43.8674 | 2024-11-07 01:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e0811292-81be-379a-8fe3-886ccba75b75 | -5.9975 | -45.3607 | 2024-11-07 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| bab359ac-9252-36dc-b974-de7478abfe94 | -17.293 | -57.5062 | 2024-11-07 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 59190a08-5a56-3390-bfe9-ec2ae838f6ba | -2.6044 | -51.3043 | 2024-11-07 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 047f809d-6c95-37ac-ba16-00afdb9c8d85 | -5.1581 | -47.6997 | 2024-11-07 02:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 21e1f754-323b-3934-82c2-11b45d6fd273 | -2.5009 | -49.1228 | 2024-11-07 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 44670a46-77b8-3d0b-b2d1-52d0fc43c226 | -2.6229 | -51.2831 | 2024-11-07 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| eac50a56-73d9-3939-ac8d-f9fac3f102c3 | -5.0154 | -46.8531 | 2024-11-07 02:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 1e600a00-e150-3400-96b2-200d83c357ae | -5.9975 | -45.3607 | 2024-11-07 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| bb7d4f84-2a7b-3d54-84f1-c7e447225915 | -4.5033 | -42.862 | 2024-11-07 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5ac0b283-7107-3d84-8219-1cc44812792d | -3.9669 | -48.1716 | 2024-11-07 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4586fdd8-f9d9-3a78-b59f-cb0ca7891459 | -5.0155 | -46.8311 | 2024-11-07 02:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 58bed9f3-261d-369c-b70d-4f96f581dd1c | -2.82 | -52.9613 | 2024-11-07 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ff0c5dfd-5ebc-3a59-91f8-0a4c8bafeced | -3.7033 | -48.9986 | 2024-11-07 02:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 209366db-66cb-3e01-8484-1a9c8d728008 | -5.0526 | -46.851 | 2024-11-07 02:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7231d5f2-7929-3591-9bae-0a36a28ab54d | -11.8446 | -43.8674 | 2024-11-07 02:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8588ee3f-3f8d-3249-bc2e-a5f2aaee6536 | -2.6228 | -51.3038 | 2024-11-07 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 75e7f4a0-7eb4-37c6-a115-d0c4a0ff8c8d | -1.1831 | -53.8985 | 2024-11-07 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 4ce47d1c-b7fd-3539-97e7-b43d29c81230 | -3.1617 | -50.2038 | 2024-11-07 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 66fd8b80-4fbb-39bc-a2a2-8a3dc42752a1 | -2.6044 | -51.3043 | 2024-11-07 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 58c4eedc-6e96-398e-8cdd-712a96aceb9a | -5.1395 | -47.7008 | 2024-11-07 02:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ba47210a-36ad-3812-bf05-efc40f3505e0 | -1.2014 | -53.8983 | 2024-11-07 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 098f90d4-445d-35e6-ae14-f8793b3fd8c0 | -1.1466 | -53.7177 | 2024-11-07 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 82cbd4e3-2896-3fc4-982e-984d3485fbfb | -5.9788 | -45.3621 | 2024-11-07 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| e32496de-812d-3141-94a9-303db8c9f77d | -4.5218 | -42.8843 | 2024-11-07 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b39b5c50-c0f3-3f94-a6a3-4c23f1bc0e74 | -2.8537 | -48.6642 | 2024-11-07 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| b44433c2-8950-3f86-855f-130f3e0a7a81 | -9.9116 | -36.2634 | 2024-11-07 02:00:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 106.3 |
| 9d7612db-afcb-31bb-a41e-f16d89363950 | -5.034 | -46.8521 | 2024-11-07 02:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8f786217-a9a0-3a78-9e32-e676195221e6 | -5.0342 | -46.83 | 2024-11-07 02:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9ec8749d-3462-3dc8-82b1-ca4358268420 | -2.8536 | -48.6856 | 2024-11-07 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 187f6641-951e-3f9c-aa0f-04fe0bd9b4b2 | -2.5009 | -49.1015 | 2024-11-07 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 47562d09-162c-38f2-8f1f-50bb58171d1d | -4.522 | -42.8608 | 2024-11-07 02:00:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 7b947347-10b3-36b0-8f62-b28d75db8935 | -2.82 | -52.9409 | 2024-11-07 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| c7850f99-a6e9-3dbb-b273-56b25f2beff1 | -5.4518 | -43.592 | 2024-11-07 02:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5160e8ee-dd57-3916-8120-695642c8e3a2 | -2.82 | -52.9613 | 2024-11-07 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4144e302-0690-3eaa-98d1-39c797399d97 | -5.9788 | -45.3621 | 2024-11-07 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 273ef048-d80c-37c2-ab5e-87fa59d8d16a | -2.8352 | -48.6648 | 2024-11-07 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0439c6ea-4d32-36a6-9c40-60c19553743d | -4.522 | -42.8608 | 2024-11-07 02:10:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fca1a879-aa9e-3c21-9404-9fd3a3cb1b17 | -11.8446 | -43.8674 | 2024-11-07 02:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9f2d06d5-8226-36b6-b65a-abb6d28b9a69 | -2.8537 | -48.6642 | 2024-11-07 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| cda7ef8d-3e5e-35c4-ab86-6c0540e20b02 | -3.7033 | -48.9986 | 2024-11-07 02:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3db36743-2040-337a-9093-0ad92969b243 | -3.0207 | -53.443 | 2024-11-07 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 33b96f8b-0537-320c-a550-6d975f0adba2 | -3.7218 | -48.9979 | 2024-11-07 02:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ad492766-1758-3f62-9886-5046b3e4ceca | -2.8536 | -48.6856 | 2024-11-07 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| da0fef35-0abc-3ac1-8d7e-33a338b21abc | -4.5218 | -42.8843 | 2024-11-07 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c461ccd4-9fc6-3bf1-9b04-bb8bb0ebbf8e | -1.1831 | -53.8985 | 2024-11-07 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7da0ee9f-182b-3314-9ca7-8775675c3609 | -2.5009 | -49.1228 | 2024-11-07 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 4dbaa6ea-9b0f-33fc-84b2-093c4f3d8665 | -5.1581 | -47.6997 | 2024-11-07 02:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f22d7403-97d4-3001-8e12-32193bbfda71 | -3.1617 | -50.2038 | 2024-11-07 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| becb9396-4565-338c-b16d-30a67cfffff1 | -4.6344 | -42.8303 | 2024-11-07 02:10:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| bd1a8ccf-d1d2-36af-885e-1d23f7b64c4d | -4.5033 | -42.862 | 2024-11-07 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e52d5b15-e3b7-3c6f-90c1-a7308a08e9b8 | -5.034 | -46.8521 | 2024-11-07 02:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4f985aaa-ff9e-3892-8af2-527177a7af43 | -5.9975 | -45.3607 | 2024-11-07 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 21b8a1d6-76a6-36a5-8c90-14a981d63786 | -5.0342 | -46.83 | 2024-11-07 02:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d4ee91d2-9ca8-3cb8-b7d7-6c9816f85a11 | -2.6228 | -51.3038 | 2024-11-07 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 16640702-e6e8-3bfa-9df1-b03c75d09ac3 | -1.1466 | -53.7177 | 2024-11-07 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a7595fd8-dbb1-3d10-aaef-de1d74e393c6 | -5.1395 | -47.7008 | 2024-11-07 02:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a6c65f7b-202e-3f2c-a604-f5d36d872875 | -5.9786 | -45.3847 | 2024-11-07 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |


[Clique aqui para ver as próximas entradas](README20.md)
