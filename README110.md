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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e46105f8-b86b-3f34-a924-49140fde152c | -4.95896 | -55.82566 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee689b53-7ce0-314a-8bf2-b4e69e7f4998 | -3.32604 | -59.81112 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4121890-f42e-320f-8d44-1a6155c69ccf | -2.95534 | -57.71959 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d047d19-c9b4-3229-98b8-2bd46cefe83f | -6.75237 | -59.11316 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d7a8f6-3956-355a-b399-d0698a7cf8a0 | -3.07371 | -61.2824 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5e7665-18f9-3d16-ae8c-ce32ebc5bffa | -8.48616 | -57.61703 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4333ee48-97ff-3c5e-9a6a-f874cde34039 | -8.9233 | -50.89711 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceea98f9-3e29-3be3-876e-3d894fbf260d | -3.13029 | -61.43398 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de6b824f-36a8-3722-9e35-c6217129ca18 | -6.07132 | -57.87242 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8a26c22-ae17-3980-93a3-dcb47187a93f | -6.46102 | -59.98334 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b10b1e8c-3556-3bd5-9545-7d3e3de3fc64 | -3.68958 | -60.57307 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f11e2fb6-f1f8-3bf6-8cfc-9b3185a10852 | -3.08122 | -61.16592 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ec5805-ef6b-396c-9c94-9602a4fbedec | -3.60561 | -60.57708 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa7a49fb-c14a-391b-8e8f-ac23f2e41209 | -7.08595 | -61.08535 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60e5a28c-2eb1-3170-9457-92bae54d482a | -3.92761 | -56.04846 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a24529-b5a2-32a8-b4a4-9b0d2e1a671d | -5.20623 | -56.10254 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b02a6ee1-3e68-3dd3-aecf-7de1491df266 | -6.00253 | -57.71125 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09cedb42-a114-3db1-ac2e-30d111d98ca8 | -3.20237 | -57.83906 | 2026-09-22 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41cb16c9-dec3-331b-abbc-8d83bfd576ae | -6.4634 | -59.99309 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fd53dbb3-ebb1-3847-b75c-3ee53bac5702 | -6.34875 | -59.95929 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30afaa8e-025e-3d4c-aacb-01571a7903d2 | -2.8616 | -57.80758 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d1991f7b-7717-3489-b42c-7a24c81cd3ca | -3.06098 | -61.27296 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d1c49e-8f46-3f0f-b57f-b324e2de0831 | -3.77693 | -60.73078 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca32fde9-c858-3159-8386-50f552c459c8 | -4.68335 | -55.62648 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1f327140-9591-31fa-915f-ed8a84834218 | -3.89671 | -60.59029 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48427402-df25-3a17-95b7-ac586b51d81f | -3.29452 | -57.86015 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1486ff6a-63d7-355c-9244-8ff48ae64545 | -4.78968 | -56.00926 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b65bdec4-b0bf-306a-8aa3-62c3c83c352a | -3.31158 | -57.85891 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de35050b-b451-3cd4-8643-31d08a0a5c33 | -6.06641 | -57.87586 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3c856d0-a37c-314e-861b-2f975af6eeb5 | -6.78171 | -58.61256 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91ce41a4-9e1e-3981-80c9-8d0164c513ac | -6.30716 | -57.74029 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1361042a-6e83-3023-a0f7-a2a0332eea4c | -8.61021 | -54.63086 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4af2320f-d748-310f-b7c5-86cc8dd5e630 | -5.45414 | -60.14512 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f97ffda-159b-3ae5-a3a2-15465742dd48 | -4.50561 | -59.5619 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7d9ab34-a200-30d0-b8d7-b9700f60aa5c | -6.35454 | -55.84519 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87f86fe5-e74d-3b48-ba5b-e6ba1afcef37 | -3.39546 | -61.06336 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac66b872-e9ce-384f-9c3e-5d8025c728e3 | -6.38872 | -60.02568 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48266bf-898c-36a1-9a1a-12b11468f709 | -7.2502 | -55.58229 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 361d4613-c8d1-307a-ae99-6dcc3bfed3fb | -3.06859 | -61.27027 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 025e72f9-b8f8-3e48-b5c1-d2909849a74b | -3.45799 | -60.26774 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f5cd12d-1d12-3dc2-a998-bbbaa495dd60 | -6.69311 | -60.00831 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49667cc4-8868-34e4-a7f8-8eeedf70de18 | -6.62841 | -59.92592 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 47defa23-94ca-3b56-addd-2e2b15a731b0 | -6.22463 | -56.04554 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de2e4c1a-fdb1-3887-93c8-5698358c8c42 | -3.34569 | -59.85347 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 507e1c8e-a44e-3338-993f-cf981563d5aa | -7.8709 | -54.73874 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 217f6f13-51c5-30b3-9cb1-aa831cb692fd | -8.62644 | -54.63663 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e71cabe6-421c-323a-b1ad-ae38c9554661 | -4.08934 | -62.08979 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf2acdad-c8be-3c75-9b79-c39b11952999 | -4.26975 | -55.44577 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7606be8-0ddf-300c-893d-53830ff40638 | -6.45963 | -59.99255 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1c6b9969-0a90-3427-9fde-76261250584b | -3.41769 | -61.29984 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22dde39-4303-33fb-9861-1ef8270d235d | -3.22421 | -61.05652 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcbd1aaa-846f-3eb7-81e5-fa24b16507a2 | -7.6147 | -55.35831 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e395fe60-ccf5-31b2-9290-9ede0abce607 | -3.40456 | -61.29403 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a8fd6a7-1b34-3b61-9afa-51c888ce418e | -4.67841 | -55.62598 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d22c68bf-8b7b-373b-be9b-e6b786fd15de | -2.86215 | -60.91039 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4ce371a-c566-359d-b3f4-6e2ca1cf969f | -6.62702 | -59.93272 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9516d8fc-6a94-3e9b-a4ff-a00af3274a85 | -5.88533 | -51.57758 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ac57373c-af71-3073-be82-657290e243c6 | -6.19128 | -57.7748 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18413a08-ef45-3dd4-ab6b-8b9e7b56c2a2 | -7.60899 | -55.35637 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ee844c3-8505-3256-8b79-6b835b0d4c3b | -3.05735 | -54.40632 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d17cbf-bb56-3a53-912f-a39f72032d17 | -5.98574 | -57.70478 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c959fa28-2b57-375d-8e1f-4088812ee05e | -7.61161 | -55.34162 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f8800c-5528-340c-84b6-6e8359076c2e | -7.60558 | -55.34281 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df24c366-9855-3cc5-8943-2e41d99097c9 | -7.60596 | -55.34399 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c86c157-83b9-32dd-926d-42d7e4737145 | -3.08407 | -61.17018 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a26d4913-b2da-3dc5-b6ab-6eac0019c89a | -3.38401 | -61.29087 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 270cb712-7864-31e6-9a5c-c0459d91e17e | -7.69562 | -61.54169 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b000b443-dc91-3499-b6b3-53ba54871f6f | -4.5187 | -55.75976 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1702734-130b-3dab-ba29-be01323e1687 | -5.80974 | -57.7362 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ed1e1c3-fdef-3383-96f3-a8b2918f2434 | -6.71245 | -58.99682 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e918c4-e24d-31c4-a978-51b31ba47c33 | -2.7927 | -59.8967 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961cce84-d0a1-3d87-8600-933c060107f8 | -7.61079 | -55.34365 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7eff1d6-5ada-3764-bd1f-b57e31ff185f | -3.15363 | -61.39914 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01dc241e-13ce-36a5-8fd7-ee4d256f0130 | -3.46276 | -59.52662 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ed6c34-e0b7-33cd-a878-dc75f216f993 | -6.13881 | -59.94104 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed09831a-ae69-3e17-a64d-4308e66be572 | -4.86873 | -55.84314 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 854a8bda-216f-3ade-a75f-aa1a58a948a1 | -8.61725 | -54.62057 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 327cc1e2-ac7f-3c6e-a593-be083cdd65e5 | -3.32924 | -60.72453 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f18a98d-cd0d-3226-856f-1503e4c420e7 | -6.46687 | -59.97009 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c17711a1-35a6-3409-88a5-810e75b18c33 | -6.34807 | -59.9638 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b666e2c2-3b5b-364e-bf82-b50aa97430fc | -5.9164 | -57.68302 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe4915fd-97a3-3828-8e19-8f513b0176bd | -6.10049 | -57.68613 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f50ea943-0c3c-3694-a0ae-45065aac2aa2 | -2.50611 | -59.52694 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eb1a964-acda-303f-9c30-7156acc02427 | -8.91266 | -50.92636 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcd6f581-83db-3cec-8b2b-40e4854319fa | -7.69621 | -61.53773 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc8c0b46-e81f-3c3b-b2e9-63c08d1027e5 | -3.68896 | -60.57704 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f95bf0a-d898-3182-9124-ad4144563e35 | -6.39318 | -60.0217 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4489dc-af76-3d24-9429-91c6fb60662e | -3.13549 | -61.40109 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd59993-4131-368f-98d0-26d6735aaf55 | -5.80419 | -57.74398 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2ae6ccf-1424-3da5-835b-0961e9335b88 | -4.96791 | -55.83224 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6487b83d-5bee-39db-9cb8-0805426ac3fc | -6.34823 | -57.8915 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4cf8612-e11c-3008-b78b-214c9c9bb679 | -3.34438 | -59.86194 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbec5353-50e1-39c1-89e1-c7d800cd718d | -3.48944 | -59.57601 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4aeb8ff-b3ca-3909-854e-8be13b08e098 | -3.90358 | -51.88787 | 2026-09-22 05:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5390c63-d471-3288-874b-fd170b1bcf95 | -6.08137 | -57.62833 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3f823a43-ed10-3122-9623-21af33c428cb | -3.36703 | -61.28867 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85ffa70a-cec4-3b2b-93cb-816de4aaa91c | -5.38051 | -55.90541 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3b8f93e-b7a7-3cec-84d0-e2de34d31786 | -3.75637 | -59.42544 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae35865-4e90-3f01-b1d5-e1675b2924f0 | -3.04222 | -61.25872 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef99c727-b883-3bb3-955d-6ea8353cd255 | -3.06798 | -61.09532 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README111.md)
