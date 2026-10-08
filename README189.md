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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f10af2-b072-3fbf-b4fc-1e592953a6dd | -2.57569 | -56.17896 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d77e1024-2eed-39b3-8136-4024d6b4d79a | -3.06242 | -59.26626 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38ca3ddf-9869-397b-ac81-167494a896a0 | -2.78415 | -57.64795 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5db88670-2b5e-33df-9058-396bf4e8c44d | -2.84078 | -54.13283 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac8fd871-600c-3788-9d48-e096fa48d562 | -3.36285 | -58.19041 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2746a7ab-97f2-3aba-96c5-8a8550785fa6 | -3.26259 | -54.04513 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13f8d88b-0e9a-359d-825f-c05164c7dbbc | -3.29132 | -54.03604 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 380de0f4-024f-3bce-9c5d-36cdb8a95fb3 | -3.85197 | -55.99147 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d6340c5-a629-3e46-9caf-2613882b8b94 | -3.99231 | -56.26603 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d09a3e72-8254-3599-aae5-9daec5056a76 | -7.38937 | -55.21475 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa77bd2f-bf8d-39f9-8cae-acfc484242a9 | -5.28739 | -60.09487 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14b229d7-619f-3e23-928a-fee6d294235d | -3.58243 | -54.66455 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dd2e457-4fa9-348c-973d-ee17cc8ee088 | -3.16325 | -54.73339 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97ab1aef-36dc-3775-b245-db7c4c557721 | -4.57614 | -54.95498 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf09d741-b978-3a94-8fcb-f2a88841bf56 | -3.24078 | -56.80492 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e6db4be-48ec-3311-98bb-164be50d4ad1 | -3.21877 | -54.29867 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c55248d4-02a1-3a3a-8712-ce5e06f9fad4 | -5.73872 | -53.45638 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4378118f-4fa4-36e0-8de2-7643b71d442e | -4.06865 | -59.84864 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 801f72bd-4835-313d-b12f-73a516af6592 | -3.17712 | -54.7448 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59df7a8b-f4b9-33a6-b96e-9b3cbc023c50 | -3.10724 | -53.77518 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f810037-bc43-3a64-bb70-1ac771b71bb8 | -3.98757 | -59.21484 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec94441-9ad8-378c-9a29-a95f361c08d2 | -3.9795 | -56.22475 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9cc7dff-89ad-3a51-aa9b-dae01a49a83a | -2.94541 | -54.15521 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e90bc683-2196-3229-bfc2-e601305accc4 | -3.65061 | -54.06165 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0f50913-f8d7-34c7-9999-84ff1c94edae | -3.56261 | -59.4883 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14074208-5375-30ea-9835-d7130b05a9f1 | -6.4832 | -55.29942 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b4a090e-ca91-33ed-ac96-84956e9273e9 | -4.34109 | -55.13137 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b2b4a4-26f2-30d1-befb-6839d59d75ea | -6.99674 | -59.1167 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db80f9d6-fa98-3b1b-b8ef-ca05720c1884 | -2.84746 | -54.1301 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be71cbdb-881a-39f0-9c6c-0fb85e00db59 | -3.65985 | -60.62488 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b8ddc0-cdcc-35b8-ad0f-e348afe31239 | -3.12046 | -53.78792 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8e3d8b9-2392-3b52-bd62-78dacdda6429 | -3.17189 | -58.62642 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39d3a281-8793-30d2-be8a-4165e532041c | -2.77825 | -56.50724 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39aa8aee-2793-3b62-af6e-d00aa8b9b553 | -3.4963 | -59.26304 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c0a932c-3cf5-3d27-8383-34b65943e40e | -3.07853 | -53.95296 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d5f05bd1-1cb2-3237-9299-80729bde3264 | -3.26405 | -54.03554 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38105798-116c-3535-beca-c451795284b6 | -2.86916 | -54.1598 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43813a90-8139-36be-97cc-9a851be0875b | -3.03287 | -54.10926 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a6adcd1-5e03-3861-978f-b8853ee0bbeb | -3.05196 | -53.91101 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b345692-5ee0-3c03-a189-22de275e92c4 | -3.545 | -54.6686 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4101fa89-1b85-3bd1-834a-21b44158cf7f | -2.50485 | -56.1516 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4185d8a8-dc8b-3119-88fb-5eb1305b7626 | -3.10077 | -54.18989 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c01a591f-47bf-300e-b089-03ea003d4c49 | -2.94012 | -54.15445 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efc1d28e-0ebe-3645-a146-f66df6b7fa4d | -3.07299 | -59.2725 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e42da7e-e730-38cf-ab33-6bf267342504 | -2.58095 | -56.17505 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74cf9fe0-d136-3813-be2c-8d0ace2ecc72 | -3.10246 | -54.28608 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5a464f1-e761-33bc-81eb-f7ac298f1116 | -3.91175 | -59.10514 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| abbbde18-f744-3ca6-9be6-40d24dfd1c16 | -3.5116 | -54.6308 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f52bee5c-03fb-33f5-a13f-1ffc61044a7d | -3.66522 | -60.61361 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1944250d-3301-3265-a283-d5d5992cb063 | -3.17385 | -50.45282 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 452330e5-ddd0-3a09-863c-1d2a5967157d | -3.98409 | -59.3376 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 582b72b2-e320-371a-898e-c6e0ceee28a4 | -3.38545 | -59.42918 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29a00544-76e4-30b7-a2f6-e27492f09a16 | -3.08006 | -54.2924 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36c18d19-c195-390b-8e9f-25140f7509b2 | -4.31543 | -50.77965 | 2026-10-08 05:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9600771-8fb6-3d88-aff9-f55c34866be8 | -2.94142 | -54.17873 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb9858d0-4d9f-3304-a1ab-6327ad2f2eb4 | -3.28137 | -54.06532 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eff437f-5101-3c3a-b199-a45a7822c666 | -3.5434 | -60.20526 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 911e3e4a-3ba1-3239-8bb7-ae8e4a2098de | -5.06769 | -56.90939 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed2b224d-e12b-39a0-acef-b493ed5e193d | -3.58528 | -54.68066 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66619af7-4b9f-3505-ab0b-f619f4f57745 | -3.22921 | -54.30062 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99023f13-96a7-3ba1-ad64-049b3dfe425b | -3.06113 | -54.20702 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb98f457-95fe-3ab2-8fd5-26def3594b48 | -3.00846 | -53.90785 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aaf7af4-255e-31b9-a557-ca140b17676c | -3.18321 | -50.55278 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3db98edc-08ea-3bec-941c-3c09ccb0b18d | -2.70386 | -56.54554 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3dbc3fb-1601-3ac5-8f90-663d695e4eb8 | -3.54074 | -54.66177 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec9d466-e90d-3ec4-8a9e-9a9cd7ba2e87 | -2.50796 | -56.16174 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f664441d-96f1-3874-8f50-72dabe0bf059 | -2.78342 | -56.50346 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed5395f8-7b4d-3c21-ac90-fdb896f3bba1 | -3.0896 | -53.93412 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34dee609-095d-3902-9b79-dd9f9fc0cbf0 | -3.00546 | -54.075 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| cc299eb5-cfe5-3e34-aa6c-f3079c39a55e | -3.70424 | -60.54944 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dea5b7a4-cbed-353c-b572-51af30160e7a | -3.79276 | -59.32279 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae79e5c1-fc5a-3a95-b471-cdf900e9f5b3 | -3.10088 | -53.77077 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09665a6f-c26b-34ce-8ae8-54306fffd61a | -3.11165 | -53.78304 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ef6687d-4893-3a1c-b069-b573e58cbf63 | -7.38326 | -55.22014 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad77d686-0a61-3576-b634-9b0e1a729e39 | -3.43301 | -59.62851 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a41b7e7-3c82-353d-858c-7eb213bbf923 | -3.29876 | -54.02324 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 228cfcfa-8f43-37ef-bdef-9081e2fa0cba | -3.28949 | -54.03247 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9656648-6101-357e-a9a8-7dee59b03365 | -3.0125 | -54.13649 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeef43c3-8e33-3013-94cd-5a0de01b8911 | -3.05537 | -54.20944 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3959473b-87ff-35ab-bf5e-153b38c18046 | -6.43221 | -60.0569 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39005177-a62a-3725-a87a-fe5322fc832c | -3.11451 | -53.79055 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 781175a8-789a-3355-8fbb-b030011d9ecc | -3.09818 | -54.27886 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 461b391f-a802-342c-856b-870c81313bc1 | -3.83933 | -55.97936 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1713e31a-c7ff-3fcb-90a5-80299027159c | -4.9356 | -55.81588 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67199fa3-52eb-3cb3-8ecf-e1296bbc6ef9 | -4.77258 | -55.73331 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17dfdb66-130d-3fd3-91fb-c0858859edc9 | -3.47304 | -50.08556 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6111365-2439-3949-b93f-38bd2a7b17f9 | -4.44736 | -54.97489 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7d3f76d-bf66-3958-a647-f64fab7c409b | -3.85349 | -55.98149 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2fcf703-871e-3653-8ba9-5d43788a8ab5 | -3.69341 | -60.5491 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 180d232d-2821-3088-bce6-b762533ca610 | -3.29387 | -54.03998 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2933419c-84ea-35ff-84da-d5d4bc380805 | -2.99868 | -54.08406 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 13ccc294-cb49-3807-94ec-1979a47a3b0b | -4.77855 | -55.74623 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49226965-5a63-3b75-8cbd-e3249284e45c | -3.2694 | -54.03632 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff2cb06a-8d9a-3775-9ada-7ba98c3f0d15 | -6.43596 | -60.05746 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12c5f22e-b952-3128-8074-82c5d7384c24 | -2.78134 | -54.06681 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad90214-8b97-3b87-8ef7-f741bfb2ad96 | -3.11893 | -56.66523 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc6063ec-529b-3767-99cb-a731c9d378d7 | -3.40172 | -60.84108 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24916f5d-5afc-378f-8ba0-6a0ded61276d | -3.73281 | -58.86223 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67dcb5e1-75ab-31e3-94ff-94d889f84936 | -2.87772 | -54.17471 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 228a3329-0fdd-332f-8736-82a05046dea2 | -6.46812 | -55.47923 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README190.md)
