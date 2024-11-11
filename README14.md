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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f00d5c2-8b51-358f-81b4-4358814f35ea | -2.2306 | -46.436199 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 932ff853-ae33-3ade-b6d0-9823e6751188 | -2.8657 | -49.512901 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1104700-80d7-3d09-9902-d5be13bc6015 | -2.9066 | -49.2444 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e1f46b-7e16-3d72-8a40-a445e5a16f29 | -2.2594 | -53.7435 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 214de06f-58e8-34db-8e97-ff0118251ee7 | -2.4481 | -51.953499 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b293616-8856-3dc5-8754-fa8fac139666 | -2.2175 | -48.852402 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e4a2b4-72d0-3342-9a82-ca72b595aafe | -2.2349 | -53.771702 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a01e440f-e70a-3bdd-a583-45494fdfba06 | -3.2536 | -53.402199 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a36c5a-ab20-3580-9dfd-f72a6671f024 | -2.5424 | -47.327499 | 2024-11-11 00:51:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e99feec-3655-38b8-8784-78316e00ce86 | -1.2113 | -51.779099 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3668f510-5dda-3b90-95f9-ce9198783ae1 | -3.3809 | -50.134102 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36748f8f-a799-31de-9800-8c4c3c14613e | -2.4399 | -51.962502 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7b4744a-86a6-3c09-81b2-7835fe1f4e64 | -2.5658 | -54.726898 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 926cc5c5-4f7b-3a74-8dca-3adb60c39a74 | -17.249201 | -57.4828 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1a0b59e-f61c-30fe-98e7-dfa3d95596ac | -2.4465 | -51.946701 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335a43c7-0f7d-3b0e-8f27-222742100052 | -3.0996 | -53.902901 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdf17ac-9b3f-36a9-abb6-8e7af6db05bb | -1.4826 | -51.7472 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7beec724-83bc-3d7e-ab4e-4c56161bdd6c | -1.2408 | -51.772499 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceba9302-f680-3011-9ee3-8204922d1561 | -2.5549 | -54.000099 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1342f980-c767-3e69-82fd-a86d26196150 | -2.8347 | -49.423401 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b4c0b24-ad17-344e-9470-ad6c9f7ddf40 | -2.1985 | -49.526798 | 2024-11-11 00:51:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acfdfcc1-0e94-37b1-9d43-0d5ba729d99b | -1.328 | -47.7285 | 2024-11-11 00:51:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae23e3b-0592-3f15-ba63-7eb5d3db9221 | -3.3073 | -50.128101 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e4acf0-a746-3fa8-9cfd-364521a48aba | -2.8926 | -49.361801 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 465fd673-9438-3a07-930c-83ae6aa79d16 | -1.2212 | -51.776901 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 945b7886-1aae-33bc-804b-28c50acf1181 | -17.6199 | -57.5331 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46ca97da-3f11-382e-8057-3fb0b587b80a | -3.285 | -53.676399 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497b8515-0fe4-300d-8678-a171a3a04943 | -2.7428 | -49.338699 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cef0c0f-0922-3171-8bbb-313626e3c104 | -2.75 | -49.369701 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab6baee-4747-31a4-88d3-ec911331ec88 | -3.0152 | -50.963902 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11108600-3936-330a-a9b4-e88579e39251 | -17.592899 | -57.438 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4cfb1af-4983-338c-95b2-2af0071e9ac8 | -2.6538 | -49.399601 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5973b976-a379-3550-9688-0cc946168a1b | -3.0886 | -53.311298 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e837533-64c2-3e0f-a46f-809b9ea6d610 | -17.236 | -57.4655 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 142832d2-dec4-3f27-bcbf-700438084dae | -3.6755 | -50.203201 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a534845-02d3-3632-a4a6-a60aa67a60be | -2.2193 | -51.990299 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00711113-38dc-378b-a151-b51bde8f26ab | -2.9922 | -49.5243 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67cbfad4-3b1c-3d63-b76c-278c6a305ef6 | -1.6243 | -52.544701 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e56631d-3565-3550-9769-326cdb67f4c7 | -3.2262 | -46.2066 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97dc9341-1648-3fc9-9372-ecee9f98d1d2 | -2.6074 | -54.004002 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4c7ff6a-e8c9-30af-93ad-dd788bdd7f6d | -2.6314 | -49.525799 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d46cc36-629d-3792-93a8-7e85fc3d4c74 | -3.2407 | -46.486198 | 2024-11-11 00:51:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8af3ccd-2654-3bba-8c79-5b73b55f7d7a | -3.0828 | -49.559399 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7aad977-678a-3d06-87aa-a200c17f4803 | -2.4485 | -52.224899 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac32ad1-192d-3c7e-90f2-1b7e4eb5db68 | -2.307 | -53.816502 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af21ea1-151a-395f-b456-182910337a3c | -3.2085 | -49.522999 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b04c0cda-65ac-3346-8381-e51d88ae3fdc | -17.633101 | -57.5508 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca561aca-cfe3-3448-ab36-104c5b97cfe6 | -2.8445 | -49.4212 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11479690-17c7-3929-971b-817886f123d8 | -1.1441 | -53.780499 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3209c09e-4cd9-3cd7-9d42-ff52926e909d | -2.1234 | -48.891102 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a710d0ee-1826-3401-accb-a29e85085587 | 1.4883 | -56.009201 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec30c9aa-fd73-38ad-95b7-e5446826bbf4 | -1.4187 | -51.110298 | 2024-11-11 00:51:00 | METOP-C | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d0b0ba-7561-3d22-bf3d-96e2bd73e757 | -1.2376 | -51.7589 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 306864ba-1e70-37b2-ba57-13dd9e2731df | -17.593599 | -57.497799 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f1660c6-626f-39d1-a424-c7320c886f57 | -3.0699 | -49.370098 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924797f7-2bc7-3750-a91d-93ef9e5dd748 | -2.9514 | -49.348499 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61e97b7-04d2-36be-b70c-f9ec5cc9c742 | -3.1823 | -54.312599 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bde82349-b16c-311f-b088-814696188084 | -2.6223 | -54.024101 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5006f259-b874-3966-9c68-df02268c25dd | -1.778 | -52.360199 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04c2d192-63fb-3e2d-b5ea-3c251f117689 | -3.2659 | -51.606098 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823776d8-3e5b-38fe-8f35-54b1944274c1 | -2.2465 | -46.504299 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46344082-1cac-3e73-b49a-560106174b4b | -3.2276 | -50.498001 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cada65a9-0c17-3f8d-b0ce-b36c836f4d52 | -3.236 | -46.204399 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0838e322-05cc-323e-b332-381e1f2aa068 | -17.2784 | -57.477299 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef0a8ad8-b7b1-3b86-965c-947f7984b7c8 | -3.2397 | -53.069801 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a62a5329-7316-3045-af87-33777bc0027f | -17.2915 | -57.494598 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a779d7d-581f-3af0-b033-5f156f690f73 | -2.7642 | -49.342098 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3d7a39-6e83-3eb0-89c3-9dca15b8bf36 | -3.3071 | -50.0826 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f067fdb-8a13-35ac-bcb1-c350264cae71 | -3.2433 | -48.740299 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5414b26b-aa29-39b9-9bde-095479d7fcea | -4.0765 | -43.952301 | 2024-11-11 00:51:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26ba02ff-936b-3c6d-8c66-ed41e8a37f5a | -3.0218 | -53.244202 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe2fac5-d752-387c-aa9a-50e5925f0c72 | -2.0624 | -53.287201 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec20fa56-1e66-3bdc-917d-3d0a4c051b9e | -2.9889 | -46.991199 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982be112-f740-3aea-8005-d3b15fbef786 | -2.3491 | -48.5312 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075649ff-7a19-3daf-8f14-a34a58ac55a8 | -3.6228 | -54.7122 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a723c28e-c52d-3ff8-b370-8cd22f897ba5 | -3.3466 | -51.688202 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85cff5a5-ac96-3327-8d66-209fc7a32940 | -3.0552 | -53.889301 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45587079-fa84-39a9-8716-61ed4a611a16 | -3.9198 | -49.9212 | 2024-11-11 00:51:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4558f4b5-4882-3b98-bdcf-c8f6b7967bf8 | -3.5234 | -53.501301 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8923ea72-2d3e-3753-88cd-a98d3ac4ea5b | -1.5436 | -54.310001 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ca9156-e984-346e-b02e-5bae45b65818 | -2.6089 | -54.191799 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c45a3e40-3f2f-32b5-bf66-e9b658b49813 | -3.2647 | -48.743999 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e726675-f828-3a31-ac59-b758b22f97e2 | -2.0452 | -52.0863 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a649db95-e17e-3b1b-8ad1-779f01fa1904 | -1.481 | -51.740398 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa9f70d-9764-3e40-8075-777cb5982f41 | -3.0212 | -45.818501 | 2024-11-11 00:51:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b369d78d-6902-3a34-83c0-235b58daa47e | -2.1272 | -48.9076 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bffd3a3d-5049-389a-a04e-3f74489653e6 | -3.0152 | -53.260502 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf1954cf-3ba9-3cea-8635-9cb05d6560d4 | -2.6884 | -49.860901 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2059dd2-fcac-3dea-8745-ebfd4d26c79e | -2.7004 | -46.815399 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3c661b-c774-3603-a685-96a0d63ded21 | -1.2146 | -53.638199 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fdf56d7-6400-30f9-8be1-63ad99da9e69 | -2.8681 | -46.652599 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df852db-be77-3295-955e-ed74a85290b9 | -2.7652 | -49.390598 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca17d02b-2451-3979-a704-34948d711558 | -2.2413 | -53.664398 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 882284a8-8f2c-33d7-bcee-d677be0259ca | -3.2534 | -51.551701 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8d7ad1-0155-36d4-9647-0f1bd3aa0c4d | -2.8381 | -53.976398 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a17b766a-d973-379e-becc-d8723b0e6b3d | -3.0909 | -49.549599 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c3bfe8-d9c3-3925-83d0-eccce3d43ffa | -1.2165 | -51.7565 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1ed6ee-407c-397f-971a-2bd1cd872cc8 | -2.6618 | -49.389702 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eac32d8-832a-3d7f-a5a3-af302666b74d | -2.2779 | -50.6745 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 725f22a6-271a-3c92-98c2-4aeef54b7543 | -4.0235 | -46.965599 | 2024-11-11 00:51:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
