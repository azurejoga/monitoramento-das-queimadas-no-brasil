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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43bf1cca-86f6-3206-918b-9a43238e33aa | -20.40108 | -43.11115 | 2024-10-04 04:12:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c7455ccc-1f4d-3d8b-820f-5617cf035c32 | -20.38082 | -43.24914 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 133732e6-6d94-35bc-983d-b39968fa63ae | -20.38025 | -43.25304 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7600016-e347-32d3-8150-fc8dd9992578 | -20.37745 | -43.24859 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8d49b89-47fa-39d5-a1d8-bddbca491eab | -20.27835 | -43.50919 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35517a1e-cb7a-31f5-94c3-ee09369938d3 | -20.27051 | -43.51575 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d149766-b41b-39ed-9ef7-3ea5f6672dbc | -20.26466 | -43.18365 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0dbd8b5e-a9b6-3d4a-9a5e-84242cb5a182 | -20.26409 | -43.18752 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c5df4ec6-6ac7-3495-86bc-491ff34abec3 | -20.26354 | -43.19126 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e463024-ca2e-37d6-b994-fcc0973c13d6 | -20.25299 | -43.18216 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 46c7292c-0e44-3a6f-9321-a6a3f7f6f780 | -20.25286 | -43.1934 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea0eeaff-1dc2-3c1f-9854-e011b2222f7e | -20.24512 | -43.18865 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bfee23d5-f7d4-33ff-b729-4ea8b032af11 | -20.24231 | -43.18427 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 3a2b95f2-8ea0-35cd-82eb-0731a53c490d | -20.24174 | -43.18808 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 18c0a190-526d-3970-ab2e-42b7e34b124d | -20.23894 | -43.1837 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| efb8827d-a6e0-3e0d-ae67-c0551a3fe93e | -20.23837 | -43.18752 | 2024-10-04 04:12:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 224b965b-53ff-339f-9b38-1cf78cec2327 | -20.10024 | -43.4307 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 95879574-bc76-384f-99a3-1eb09dd5bd00 | -20.09629 | -43.43412 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5b9d9a66-4015-3ff6-a143-a1e84b7aeae8 | -20.08458 | -43.4436 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b266796-8662-3b94-a27e-e1b560db7659 | -20.08302 | -43.43113 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8d4945ee-6eb8-32bb-9788-70bf19946ee5 | -19.88579 | -43.11194 | 2024-10-04 04:12:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f89bb7b-0179-37e1-8de0-565e4db27dcf | -19.87618 | -43.15346 | 2024-10-04 04:12:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f3a70ff-6269-3a65-b85f-49769217d2ac | -19.87562 | -43.15729 | 2024-10-04 04:12:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6299bd25-909a-3afa-88c0-77511da72308 | -19.70356 | -42.94572 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c08c7941-bec1-323a-8b09-611cfba90823 | -19.70301 | -42.94946 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 340ac601-0493-3234-9164-9cae675b8c81 | -19.70126 | -42.93786 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8c86034c-ce9d-3781-98ec-7b2ea65a93ce | -19.70072 | -42.94151 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 47c96631-a7ed-3520-90b1-8d76b3bd1f7e | -19.70018 | -42.94517 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 728c921c-0d04-3bb4-9454-f8f2f3f1fd87 | -19.69963 | -42.94889 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e779409d-85f9-393b-9bd4-8b03869e8456 | -19.69788 | -42.93726 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 24facd77-900a-3b01-ad2b-32d5d439089b | -19.69679 | -42.94462 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e423baf4-4d85-3272-8539-a8c9e8331984 | -19.69624 | -42.94833 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b557f678-75bd-34f3-88b4-7c724c879a0d | -19.69225 | -42.92843 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 61a26109-7524-35d8-8ced-27cda93ace79 | -19.69169 | -42.93221 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 157fdfc7-58ff-3d28-948a-8537f9680e85 | -19.68889 | -42.92772 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 1eef4ff2-4b79-3b69-a3f5-17881c56b1a4 | -19.68833 | -42.93152 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| b24b6675-388d-38b2-8f3a-71265ed8ee61 | -19.68495 | -42.93089 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60b674b0-5899-3fa8-bf60-cf54ed2237d9 | -20.10147 | -43.4226 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c2c4e3f4-285b-3c4b-b304-f8adccdddc7d | -20.09963 | -43.43474 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9daec824-7053-3fee-96b3-735e2217149c | -20.09146 | -43.42067 | 2024-10-04 04:12:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b91dd9e2-9b16-38c0-8014-8e84e12c5bc4 | -20.28836 | -43.5111 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d179c565-2840-3fdc-a6e6-39d49968699c | -20.28502 | -43.51047 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 13a6e524-e88e-3009-a290-ddaa73ceb8dc | -20.28169 | -43.50983 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d288e408-d3ec-3069-b07c-2fe17e7a4d3e | -20.27777 | -43.51312 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8679a3a-2086-3a10-969c-50bc0dde5b67 | -20.27443 | -43.51246 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97413d66-d535-3d39-ac99-352c7f28ae04 | -18.99112 | -43.28308 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 56d8bc85-07d4-3eef-8408-579c2c11f057 | -18.98778 | -43.28252 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6d796488-8301-3648-823d-2938ae0812e4 | -18.98722 | -43.28623 | 2024-10-04 04:12:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d902289-2e8a-3374-8091-a5c133f19e78 | -18.88244 | -43.46305 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca71332b-222b-3d03-b91c-46703f4bed31 | -18.87911 | -43.4625 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 123362a2-9f1f-3419-8ba6-365378221bf9 | -19.28677 | -43.77517 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db2fc517-0542-369e-9940-c6f8650dbe9f | -19.28621 | -43.77882 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f402179-2c01-3119-8594-07bcd379ca24 | -19.28564 | -43.7825 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 965fc2f6-9bb7-3266-9d20-47161f708e81 | -19.28451 | -43.78986 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80d75a6f-3298-3aa3-b150-df1e467cfc85 | -19.28401 | -43.77092 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c5bd82d-8328-37c0-9c22-815619bde028 | -19.28289 | -43.77826 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 761c2a9e-504a-36af-aadf-880fb80236b2 | -19.28233 | -43.78193 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc51989b-c4a6-3ec3-becc-339f0b91f6d4 | -19.28176 | -43.7856 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa062c55-89a2-33c3-afbe-fe1d7c7a0fca | -19.2812 | -43.78928 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcbf5c7c-ef8e-3143-8dc5-8840774ec655 | -19.2807 | -43.77034 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d808ad66-ac35-330e-a85a-25070dc2378d | -19.27901 | -43.78136 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec27540f-aa3d-372a-b376-9d86add8a413 | -19.27732 | -43.79238 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee2d0e5-4ab0-3139-bae2-6291e75a1ef8 | -19.25747 | -43.7664 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9c78c7-56c7-3162-9187-0c59469427c3 | -19.25691 | -43.77008 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 742c9ad3-f2eb-3e79-b975-5cd87094c5eb | -19.25528 | -43.75848 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3f30884-7748-3013-835f-626e2d2487d6 | -19.2536 | -43.76952 | 2024-10-04 04:12:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 152c1d30-7e1d-3d0b-8a25-34c7c07a70b3 | -19.25252 | -43.75425 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64f1f587-2feb-3c10-8e25-e2ad79c290d8 | -19.25196 | -43.75792 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cc9464a-70c7-3130-89f5-0134ee0f9e97 | -19.2492 | -43.75367 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 84f8fa8b-304b-3b82-9d9a-62eebc8a9677 | -19.20002 | -43.71893 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ec8abe3-3c7b-3b85-9578-aef3717e1f41 | -19.19474 | -43.71093 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79a57e5b-8f48-3f30-a34b-5f80de07a8cc | -19.19418 | -43.7146 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3877bdb0-ee18-3b92-921f-02f4fc785338 | -19.0709 | -44.40053 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741f5f5f-3782-3ce8-9afd-bd4cfd40d09c | -19.0668 | -44.44832 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd71c714-90e1-33f1-968a-20ce9b40672d | -19.06464 | -44.44049 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 263488dd-143d-3a90-84c6-6496784c96d3 | -19.06407 | -44.44412 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67c052b2-5ea5-37e3-a902-c3dd62ebab8e | -19.0635 | -44.44775 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c2adce9-55e9-3eaf-a0bd-50c34da79fa0 | -19.0537 | -44.42367 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a915add-0111-39ef-8af6-8bc44755602a | -19.05313 | -44.4273 | 2024-10-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e13dfe-4aba-3265-80cf-1ba170ad0cde | -18.98121 | -44.1688 | 2024-10-04 04:12:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbe6261b-4386-36b7-9641-379dd9d1f98c | -18.96065 | -44.21375 | 2024-10-04 04:12:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4a6c213-82e4-3e6d-8e9c-9d090711122a | -18.95678 | -44.21682 | 2024-10-04 04:12:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3e2eea-2347-3f51-a49f-123150106760 | -18.93074 | -43.8804 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ca7e38e-5d2e-3e0d-95dc-88c739bb7209 | -18.93018 | -43.88404 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e98782-a80e-3dbd-9dfb-55228d54a19c | -18.5878 | -43.96472 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70da2b65-e4b7-36c0-92df-915ee1a3f669 | -18.59222 | -43.95806 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00988148-9746-303e-9a30-c8cb7724070b | -19.46269 | -44.13479 | 2024-10-04 04:12:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9059a55c-1e57-3b56-950d-b965c6da60d6 | -19.43768 | -44.34005 | 2024-10-04 04:12:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 820fbccf-8e43-3422-a28e-2c6fa66bb6c6 | -19.4278 | -43.8966 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b49b9e50-a4ee-3324-a54f-c27535f82807 | -19.42724 | -43.90026 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bf72257-e185-3188-acbc-d19eb08b045b | -19.42448 | -43.89603 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 06ca6397-ffdb-3e0b-84ff-dbdb6b0bab6d | -19.42392 | -43.89969 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ae221be-b7df-335e-b1ec-185b0098c77b | -19.25463 | -43.37938 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44619096-d516-3be1-ba48-4d1e7e7c1eae | -19.25185 | -43.37515 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09821404-a611-3a33-8f86-863b1b25bb26 | -19.25129 | -43.37889 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edbf0eb5-6729-373b-b964-60b33b87b5ff | -19.25073 | -43.38262 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6beb80c4-c28e-3dc0-98af-9c5c72d63d54 | -19.24683 | -43.38583 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b90e44f8-d323-3db7-a252-2661ca72acad | -19.24628 | -43.38953 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9512cc48-32ca-3fb8-bd7b-a46d587650e3 | -19.24375 | -43.38964 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80cb3fda-4200-38e4-8eec-9e4a78b91286 | -19.24046 | -43.3662 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README87.md)
