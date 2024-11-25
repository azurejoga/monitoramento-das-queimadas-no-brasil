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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b47afb24-417f-3ec7-8edf-4b627eebf8b0 | -3.70952 | -52.41854 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a76c97a-8559-3601-b2cf-8b6422ecd2db | -3.77984 | -51.87573 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e9658fc-e9a4-39fd-b150-a2146c05787a | -0.81684 | -51.49061 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ef2d298-bf43-3e55-b174-7ea4591127d5 | -3.94659 | -47.98632 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e4115dbd-f4a5-3644-97e7-ef6c698ea09d | -2.64691 | -51.774 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06a25435-231d-386f-895b-40fd7f55d220 | -2.69091 | -46.28288 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa58962-a306-3705-868e-89afc069674b | -3.42572 | -53.28294 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3052c13-ae8a-3a37-9a65-0353ff4fe149 | -3.92402 | -46.40005 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6dddb0b-423d-34a4-a7c4-45e61bbad245 | -2.32093 | -51.3144 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 299a1c34-6108-36dc-a6be-578b0572c219 | -3.64085 | -50.2238 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9568e15e-e974-3edf-868f-f454fbacad74 | -2.87711 | -53.99387 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00869447-d625-3805-8b1d-3d017e9f20f3 | -2.58359 | -54.04835 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d862cf9a-0dff-3d75-928e-ec2b29cb8f72 | -3.26671 | -53.81678 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de06235f-4747-3a7e-9f96-0d32eaf52f52 | -1.92631 | -53.09073 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ca971e0-af05-3047-a42b-f382c54c5330 | -1.22248 | -51.7967 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54a5e712-19b8-33c7-ad10-eafcf8ad0c22 | -2.78772 | -54.04058 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc7fb9b0-e673-3739-8377-22bbefef6d7a | -1.73373 | -52.72208 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 922fd9a8-46bc-3c60-8be0-c0e04d3ab5cf | -2.80208 | -53.00897 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c7fd60b-9287-346b-860e-48aad253d605 | -2.87235 | -54.79837 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c3db63d-010f-3154-8c17-69d41675434d | -3.47524 | -47.68233 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095ab539-cd02-3d8d-8162-bbe8e4d7d955 | -0.33965 | -51.54117 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc2b36e0-35a7-3e25-ac2f-4fc1da51c3fe | -2.73464 | -46.11004 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d3e3148-a432-3c93-951f-4de43cff26eb | -4.54839 | -48.95529 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bbff4c1d-7455-3b3c-a188-59ea3b31e588 | -0.25752 | -51.6478 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2675f3a7-5a08-3547-8c8f-d3a34c8f718f | -1.83061 | -51.21018 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c48b477c-ed6f-38bf-8041-17785639c40a | -3.3014 | -52.86352 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7780dfdd-1cb9-3ae9-ae0e-ca19f0e5288e | -0.88223 | -51.71925 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c619e665-2a56-3340-9269-d4fc29411cd2 | -0.95161 | -51.71553 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 032cd40d-6156-3733-b35a-45e542b2a19f | -1.36964 | -52.0861 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20274bf1-d5f9-3765-97ab-100deddea26c | -3.02348 | -54.04926 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c78039d2-4341-3edb-abd1-b5d8bbeba7c4 | -1.30542 | -51.73672 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1ef56f9-e73a-33a5-bfee-9a1df0e3e436 | -1.36533 | -52.54788 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 195bc60e-3342-3429-bcda-a17c18a187e9 | -3.08304 | -53.28622 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39e44cf7-c264-3d18-9702-65511659daa1 | -4.29699 | -46.90548 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c3a647da-f2dc-3d51-9b37-c3c9601180d6 | -1.39463 | -52.05771 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06170e91-98ce-324f-9a6d-b03ff6bc75f6 | -1.60918 | -55.12853 | 2024-11-25 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa1443d4-b9f9-3323-b2f6-f6f0138da85d | -3.1915 | -46.37027 | 2024-11-25 04:55:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf4884f3-b30b-3e08-b2ec-97c74ff872d7 | -2.01661 | -51.18599 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc502901-c20d-39bd-9286-1f4b8be77bc2 | 1.41136 | -55.88928 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58d493b2-5a30-3d79-86e1-d9c3fb9c887f | -3.2281 | -53.93149 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac9bee0-934a-3098-ac40-742ff76ef60b | -2.54219 | -53.99179 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32e60e64-2949-300a-abd7-1dda00f7f874 | -3.49497 | -54.02339 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ac2d30-2306-3f00-b079-f8de8dfb29b4 | -2.54953 | -54.05382 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 627283e3-4bff-309e-a7ce-12c154d60276 | -3.12745 | -54.18336 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9a999e-e608-3ad4-8082-886953d3e966 | -3.31491 | -52.7554 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c64fff04-c277-3ae9-ae85-b7ed88c0c3ca | -2.21047 | -53.66917 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 368e5e22-3017-3fd4-9165-f909908bf563 | -1.88665 | -53.321 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c89fc632-23be-30c5-a8b9-6c6c87ea044e | -3.29075 | -53.6647 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b4a465-6d30-3667-ad9b-30b052903068 | -3.23843 | -53.63179 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c95f8b9-6542-3496-843f-30a9d5ab2f82 | -0.98749 | -51.71731 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb61aa14-711a-3ae0-ac3a-1e954bf411b6 | -2.8894 | -51.58463 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e98c8497-ee6a-3d2b-af18-8c7bc1a5fae0 | -1.22799 | -51.73959 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2fccfa7-743d-32be-a492-56feb9ff68ea | -3.65843 | -54.42462 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06bc62c-6dc7-349e-ab44-48bb4b9c5cf9 | -3.51564 | -53.82775 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccfcd7d1-9beb-3f0e-89ce-0370db04a541 | -3.52359 | -54.79584 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 129ad836-b3dc-3771-8bdc-d85e68719f7a | -3.02403 | -54.04577 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77c80433-3601-3c93-a82c-69449622f41f | -3.10333 | -53.73824 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c86262a1-298e-3c84-9ab1-7dc69272466d | -1.13327 | -53.69639 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9177ecf2-3f35-365a-b752-51d2593620f0 | -1.4923 | -52.51434 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a19ead1-8380-3cc7-8996-3a721b966ca5 | -0.88168 | -51.72278 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 387f85e1-784f-3ce1-bac4-927a9c635fdd | -2.3261 | -51.30385 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 476bc170-bd02-3ee6-b9af-6c6bde504ba9 | -4.24374 | -48.63145 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5161072b-e8be-33a2-bc08-1b00b74d3f2c | -1.38026 | -52.32322 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 294b08d4-882b-3e6f-b8d7-8b1cd5d97848 | -3.51064 | -53.81631 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 791b3f99-9543-3595-8ef1-83db705229bc | -3.97683 | -49.97074 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 071c363f-5606-3249-9d78-69cca0e9957d | -0.91078 | -51.73454 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ebd48f6-cac4-3eb4-ada4-72e8bc5e0be9 | -3.27401 | -48.75866 | 2024-11-25 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 245ff929-47e6-339e-a6c2-8813bf775d44 | -3.71752 | -43.87052 | 2024-11-25 04:55:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31a8ddb6-9618-3194-bfef-b523fdf3e750 | -3.24734 | -54.24146 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dec00d76-9966-3b16-8759-16519788b28e | -3.28174 | -54.17529 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80713a96-7858-39bd-9044-7355cff9e417 | -3.73442 | -50.43671 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a461127-a87e-32c5-a9b9-c0978ecbed1e | -1.06756 | -51.75507 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53a61ca1-b4e2-325d-9dcc-baaaa0789a6a | -3.25568 | -54.23199 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d95a6f7-759f-35b0-8b50-bf594b51f967 | 0.95034 | -50.75534 | 2024-11-25 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae54e377-06f9-3e0a-82fd-0be3c1623cc6 | -2.57744 | -53.97938 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73e6dfe2-22c8-32fd-8f10-c01e9e60f4a7 | -3.28393 | -53.83717 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 986bd5f1-3d98-3e1d-b405-9f7f719d570a | -3.29186 | -45.73289 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a07f37d6-be1b-3d11-85f5-3facba8a28cd | -1.56876 | -52.28462 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e95966-5ad4-33ba-9107-29d0410abb53 | -0.35569 | -51.97496 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84db8fe3-fe11-324c-8c4a-7cdacfe35e00 | -1.23367 | -51.7912 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd69939e-6110-3f8b-8719-26f25143204b | -3.85308 | -52.14542 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac88ba1-f577-3ec1-bd92-75fe6138d99c | -1.6268 | -54.46479 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd26c67-c062-3070-86f6-e741b44789d2 | -1.71883 | -52.73037 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 255b22ea-52a3-32e0-a756-5f778017c96b | -1.73948 | -52.79362 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1417daaa-1113-3ad8-981d-4ea55249f2f4 | -2.85708 | -53.96934 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9be1ee9-6986-3d75-b9e2-b43e813a5ff1 | -2.74744 | -54.02007 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f234813-1019-3c53-bd19-db82da95756e | -3.74113 | -54.6725 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81bf2640-2c0d-3070-ae6d-d90e6a2db21e | 0.95092 | -50.75898 | 2024-11-25 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 989f4954-4b45-3667-9f83-fe1c44f85055 | -3.50509 | -53.80833 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f636bc-4b87-3044-86b2-956e80bd1b9d | -1.76857 | -52.71689 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d28855a-3db4-3524-b5bc-2fa63a062adb | -2.86374 | -53.97038 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 182fb513-a24c-387f-9bbc-2f454a2fc49c | -1.04742 | -51.75195 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783e53cc-1595-3c85-b0fa-4ecc445784a7 | -1.60031 | -52.23603 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ab41a0-a23a-32a4-904f-7992155c6a70 | -0.94877 | -51.64617 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8cd55be-76f4-3739-8ac7-34008a77ee08 | -0.89377 | -53.00328 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ec9ba09-6f69-3e45-b76f-cdb153cfee94 | -1.7708 | -52.72431 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74dd7788-0762-3b91-97eb-20401ec65f69 | -3.26895 | -53.82421 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89e01de8-6128-364d-90bd-a4a8c9810f6b | -3.71078 | -51.80133 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ab33d67-174d-3a72-819b-3758c27abd05 | -2.89895 | -51.76844 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8715c9a4-4e65-37ba-91db-8e475c114a63 | -2.99856 | -53.73604 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
