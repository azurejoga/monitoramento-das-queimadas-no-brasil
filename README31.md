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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e63096a-5b21-3419-a150-52d0c992f2b5 | -2.99534 | -53.01853 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfd4f797-dd6b-37b5-9439-4a956797d5fb | -4.63952 | -49.49193 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 125bbca9-71cf-3e18-8ddb-e769e6787536 | -3.09061 | -54.07022 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d683e303-17b1-3817-a3c8-3c110500e061 | -2.30812 | -54.00326 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b890f7e-b457-39bb-a04b-2aa17612c508 | -2.22366 | -53.72281 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f57e4ec3-433b-3ca9-b7c3-a8a8dff5d569 | -2.79011 | -52.86915 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6375fa82-d2c9-382b-8e6d-6154b0a3131f | -2.92211 | -52.95961 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a448afcd-5b30-3d25-9b9c-76ab91294453 | -8.43937 | -49.62904 | 2024-12-10 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf03baea-6f96-301b-bbb3-fb9172e90de3 | -3.71561 | -52.44601 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a61187f4-5a72-3c7b-82e6-66e7916d5405 | -3.52801 | -54.59179 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b051469a-e90e-376d-af55-ce345162565c | -3.78562 | -50.96912 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6aae7c2-217b-3d8e-a3eb-2c2f91365514 | -8.43986 | -49.62528 | 2024-12-10 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae2fb143-8bf3-369e-94a4-db9ce74ea74c | -2.47427 | -53.62671 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f5d58ea-c710-318f-99fa-490fb3376327 | -2.46882 | -53.63606 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d173bdb1-3204-3e9b-b59c-ce71be927c35 | -2.79159 | -53.24241 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57b8e610-4892-3ee7-87c5-22c1fbb62111 | -5.91668 | -48.05817 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 058bd3dc-5e27-3113-83e8-d4bb99914c90 | -5.70788 | -46.54967 | 2024-12-10 05:16:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89697224-bec5-3448-925a-59c936024794 | -3.30146 | -53.85935 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b1251d5-3fd0-3c26-a0c3-44a3af7bc42f | -3.34063 | -53.25333 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 195d2b0d-1a2f-3de5-a05b-044edd43f37d | -3.05646 | -54.24596 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e5fa11e-e31e-3da2-bcb0-f4011a16e2f8 | -3.52527 | -53.32084 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e5ec3ae-fbf4-33ed-9d29-1ba902793cb1 | -3.5291 | -54.68968 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e7c0e2e-59bb-36c7-b8a8-bd67abb8f63a | -2.77234 | -44.99652 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2237e08-6587-392b-be7b-4f6f369e2b5d | -3.37134 | -51.19699 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d253600-7411-3f19-9160-0eb7217dbb91 | -2.99114 | -52.85252 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4303ce8-0983-3432-8323-a4a16bb34bc7 | -4.38744 | -47.76452 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2b134fe-5ee9-39b8-8ecf-d52c266e51da | -2.62609 | -48.05663 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e5be46c-753d-3b01-b5df-efd9c72035e2 | -2.9917 | -52.84881 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c1085cc-10c4-3eda-a55e-86f97e6e942f | -3.04592 | -54.2423 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 421aed97-aaec-35ff-a66d-ff18cea648c4 | -3.50677 | -54.6795 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba042ba-1788-3318-a973-0335e2b0f3ed | -3.06041 | -54.24902 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2435cd76-132a-3d6f-ab3a-322f2c4a03a0 | -2.45635 | -53.63917 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 680efde9-c727-3a8a-92a1-d9f09deca7bd | -3.92984 | -53.58056 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae17d732-ac9c-3b16-95ba-8fd599779b93 | -2.81304 | -53.04333 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11d89a35-af07-35f3-be3c-697f66b50aeb | -7.58758 | -46.64284 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ba49dd3-d1f5-3601-ba40-ab9e23eeab6b | -2.79122 | -52.86189 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db6d9cb8-e852-3a47-8a5a-ac93e7367c9e | -3.61396 | -54.30439 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23d2a573-b369-3bdb-8472-b696da7f6b23 | -3.47485 | -52.81267 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfbd63fa-4377-37c4-92da-437d03f2a5b2 | -3.5362 | -54.5884 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152b6f5b-ec20-345a-8766-b75700ede722 | -2.8155 | -52.97715 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9b61fe13-2a15-3235-b426-bfb7a3cd6acc | -3.5287 | -54.58732 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e52480-5fde-3591-8755-b384713cc19c | -2.91745 | -52.96255 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3780431-12c8-3517-9f39-219cdb20e269 | -2.5525 | -53.42688 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd94f2e8-60ef-3dc1-ba3c-9be071dbaf54 | -4.67652 | -49.50077 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c0fcd7e-c167-31f6-8ad7-e0b8307fa32f | -2.64527 | -54.29031 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aa9a3fc-b131-30e6-b6e7-4a511d58090a | -4.4677 | -48.11619 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5d1384-424e-3b02-a677-3886fba93229 | -3.10595 | -54.07265 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23f6f29b-e59b-3d1a-8135-a8c9c8828d75 | -3.06113 | -54.24446 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c799d5de-d7d2-33a1-af50-abc2bc11e405 | -4.55373 | -48.00283 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c254268f-db41-3b74-8ad3-620f2ab0d941 | -2.78303 | -53.24456 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaa6c835-ba53-3a57-ae85-46b8c6286e77 | -3.5154 | -50.98268 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08471149-d5f2-3645-9fa3-fb0c6ddbe822 | -2.81495 | -52.98069 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1725df9c-0b59-3f81-a038-fb2402dd162b | -3.20448 | -46.81095 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19d7b69f-8187-3ec5-99ad-4e6d71fbfa4e | -2.99907 | -53.04871 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87e988f1-8a4b-3cee-8747-ece17672da63 | -2.36673 | -53.91481 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9da88f65-8a2e-3a5e-aefd-67fe5e0afa1e | -3.78623 | -50.96679 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b93a5d8-85c0-356a-a6c7-57d0b5722e8a | -3.62942 | -52.67868 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84c38841-c575-3505-ac45-89e4aabc8246 | -3.04522 | -54.24681 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1734a00-c2ec-3c29-9383-4bba6069680e | -3.63184 | -52.68589 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c07f0be2-5892-37a4-be6c-b7102f2a7162 | -2.81337 | -53.06906 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2795c78c-5c31-3ced-8675-926d9e1f14a0 | -2.31574 | -54.00445 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bb09bf9-0c86-3094-8344-151b1bc6dfac | -4.06687 | -54.16084 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb4736a-1e08-3073-95b1-dc89b9503980 | -4.89576 | -48.05231 | 2024-12-10 05:16:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70c1d097-928f-320f-b359-49b0d17b5126 | -3.10543 | -53.24739 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f5af5a7-d63c-3243-aa4d-3826649e0e1b | -1.72606 | -52.78073 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ac77d97-cad4-305e-bf89-bebd8fe517b0 | -2.81766 | -53.04035 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22c54679-b5a9-38a9-b672-3fe8773da533 | -3.39014 | -52.80723 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cad7b8d0-06f7-3b8c-a4d8-c6fcf71e1b12 | -2.77928 | -44.99744 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa75c12c-b25f-345f-a039-7e34c7fa38bd | -3.03099 | -54.18811 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcce1d20-8681-317e-bb31-8e940c997fb3 | -6.65854 | -54.93495 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcfd73f9-27c7-3b49-a096-6e7abf4552b6 | -3.03027 | -54.19275 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95c64c7-35c9-35af-975e-16c2c4f523b7 | -1.33055 | -54.632 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a753f5e-0446-3304-8d3a-ec951d1ab7a5 | -2.77853 | -53.24062 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb3eca5-f5a6-3ede-b37b-3314855276ff | -2.76325 | -54.0545 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fa2474-2de3-3d1f-93b9-2807c2524d6d | -3.46554 | -53.96322 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9ae9083-4550-326d-857b-5f252297eb0a | -2.81008 | -53.06538 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85b31021-a785-3fae-8735-43614d297152 | -3.58443 | -53.73179 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b1a8b42-4bc1-32a4-947a-32b4ade3bc98 | -3.53175 | -54.59237 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bab6338-0fd5-3d8a-ba1b-43317502d0d7 | -2.75653 | -54.16444 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c8a9a65-d284-3952-8f3b-caadc9951162 | -2.99583 | -52.84953 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c54b8d3e-6dad-3670-ad52-7c945f443079 | -3.09192 | -54.07309 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc8db752-cb63-3625-a749-3d08863b9c1e | -3.02646 | -54.19218 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea3f95e-b960-366f-b274-fb4173bc1f3f | -3.76518 | -54.40497 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4051c78b-e9a1-3c8f-9c2c-8e95a633bc42 | -1.42422 | -53.48927 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| febdbabd-ae64-34fc-8a8e-afaddfb546ff | -3.87452 | -50.35927 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a85ab885-c8d1-35d7-85f9-9d665536db55 | -3.07129 | -54.07947 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08bdffb3-9f84-3295-8333-f43fcc28f60e | -3.7771 | -50.05686 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8eea876a-1a99-3114-b1ac-767dbd221842 | -2.30884 | -53.9986 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cb6ea87-6afe-3ebf-9950-5274f6899893 | -3.17734 | -53.96631 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c7d0f1-110b-3e28-b914-2092f54bc7a7 | -2.45358 | -53.70881 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a67417b-acf6-31d1-80c0-6d6936296afa | -1.70654 | -52.60616 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 511e2fac-fb29-3ecf-b136-7e1f48469524 | -3.06404 | -54.24718 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d91ac161-f9d0-32c0-a4d7-606142f52aef | -4.39221 | -47.77383 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6499147b-206a-3e85-895c-b07103d97e6d | -3.27658 | -51.07968 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19386b51-d23e-3766-94ab-aceed6b35959 | -4.54665 | -48.01035 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11508685-96c2-3162-af3d-aded1614f876 | -2.95853 | -53.72631 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b34d73f6-c3fa-3854-8aec-e0018ca8caf5 | -4.39408 | -47.76083 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3e6401b3-e49b-3057-be43-c3d7fe8236b5 | -2.98813 | -52.84437 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a16f1395-b5ea-310b-8495-fcbec8633b56 | -3.09444 | -54.07082 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ff8fbe9-245d-399d-9e4d-1489287e52b2 | -2.58515 | -51.92267 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
