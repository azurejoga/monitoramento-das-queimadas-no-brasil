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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45eb48f2-c2d9-3142-8510-f46ac4d6370b | -3.99647 | -49.92715 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dfffa99-e518-3829-9c66-e5e49f2854fb | -3.72469 | -52.31547 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b92ce52-5317-3205-89bb-7a3eb3835240 | -3.91466 | -49.04086 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ac6a08-33e5-3046-84e0-fd92a9bfbede | -5.57821 | -42.60425 | 2024-11-21 04:31:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 092fef96-6262-3e86-a517-9a16c48bc64f | -3.29168 | -53.85675 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75bf5d73-49fa-32c4-937f-15d4cbd41260 | -5.62423 | -43.94893 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fba47dc-e46d-3ece-a1f1-2a6a5de2c760 | -4.84771 | -50.85936 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 228e2d66-93ba-3a96-a71e-8f7815a84e30 | -5.95101 | -44.24366 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9831df4f-fdca-3f45-9fd2-9b7b2a0cb212 | -3.28252 | -53.85529 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c26c6e47-0f05-35c3-ae88-524b5f308b83 | -5.66682 | -47.33619 | 2024-11-21 04:31:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36efb65d-fdfc-3d05-aa4e-edf5f0bbcf15 | -3.09995 | -53.74535 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15a6322e-7db6-3339-9068-73a9aceee244 | -4.05638 | -50.00158 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8fd70a6-7b0f-3091-aa70-b1a1e53fdafe | -3.27684 | -53.83844 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86e77794-babf-30cd-9e40-0d710f47eca5 | -5.94741 | -44.46333 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fbf0b21-232e-31d0-b885-28fbbcad063d | -3.27905 | -53.82473 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e362905-5876-3a22-a59d-8c7bdb4cb8c0 | -4.08013 | -49.29208 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d7ef3e9-89c0-3045-9b23-a2b920d6e56c | -3.51686 | -54.16904 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28199017-ef4e-39b3-b41f-98b0fe12679b | -5.73755 | -44.27596 | 2024-11-21 04:31:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 089b17aa-d420-3653-8af2-fdec20ff7da2 | -6.44738 | -49.90685 | 2024-11-21 04:31:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb7bebe1-6e51-334c-9dc3-99cb8f214df6 | -3.28524 | -53.84456 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcc63ebb-cd41-3c8c-92fb-589eebf2b87c | -3.57469 | -54.68457 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3227509a-b90c-366c-9718-11ad67af9bec | -6.82587 | -40.34038 | 2024-11-21 04:31:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a927d7ac-d650-3107-95dd-d7b0c6a6b7ba | -10.73296 | -49.53128 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 768fe19c-88ed-3cec-b135-cff7c5be586d | -4.73624 | -46.66801 | 2024-11-21 04:31:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54212862-338c-38f6-990d-49a61667958a | -3.75895 | -52.40376 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0550342-6263-3939-b917-ce2acb2e0f43 | -3.1083 | -53.75142 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 852f34cf-bea3-3143-b306-aa937d43f78b | -4.08419 | -49.28887 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e02d458-fde5-381f-b875-c3ad5338df7f | -3.9217 | -50.11836 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07ff8c7-1d9b-3c7e-991c-9dad066aa838 | -4.35044 | -45.88228 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32043dba-c303-31b0-a540-a9414420cb07 | -5.59548 | -46.53871 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec9c93c1-8f2c-3a6d-aea9-7275841ab702 | -7.17362 | -45.04074 | 2024-11-21 04:31:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c0fd368-6a2b-38b9-8033-2e3ed007ea7d | -4.94778 | -46.72206 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ecc9f37-9b8e-34fb-be19-5716a541a7c1 | -3.28566 | -53.83667 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53799a08-758b-3b65-84b9-1bbe0e67fb99 | -4.42756 | -48.29918 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31af0ae-373c-394b-91d4-484db5c5f187 | -3.38301 | -52.45444 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 337305c0-df9f-37e6-8882-9f89b4358974 | -4.05871 | -50.60633 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913d649b-e36a-3808-b991-352840fd6d99 | -4.96246 | -49.84745 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1af7287d-41d0-362d-98fb-838dc50f41e1 | -4.1978 | -48.83961 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6563cce-bc69-34d5-83b3-3eff5f610bb8 | -5.95103 | -44.46387 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57f93063-c626-3ea4-b350-77e0e497c4cd | -7.44092 | -46.63289 | 2024-11-21 04:31:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8396705-c97d-30ea-8753-f1182b3cada4 | -4.88672 | -45.83875 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e2d566-92cf-3f54-b252-854a2ab8d404 | -10.12642 | -36.45553 | 2024-11-21 04:31:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 366ded3d-cee3-328e-b1b4-d7ff99980961 | -6.29622 | -45.33928 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58036aa0-1565-3c4a-9792-ddb7901c9848 | -4.57324 | -48.02347 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a7bf4481-61b6-3c7f-a601-d38877cd7aad | -3.64271 | -52.36285 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e7d0b38-bcf7-35fa-ae86-e2eb1da38ef9 | -4.76913 | -44.49117 | 2024-11-21 04:31:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30114808-e1df-31aa-9d16-15d1d248c4e1 | -4.61247 | -48.47675 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5552c8a-e3fa-3ca6-a14c-39527b1e7614 | -3.57768 | -52.29575 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a417d85-44f3-3d11-b3c0-74616db5367a | -4.10172 | -48.48095 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00d4991-ce8b-3b51-a2ed-73b45e2bd7a5 | -3.51268 | -53.79568 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63196fbc-81fb-3d6b-9ca1-1fdc00ebe79d | -3.51509 | -54.68502 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80ed7486-d296-37b8-9d72-df4777b7723c | -4.57658 | -48.02399 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e7ad0f42-c6d0-369b-be86-1b699d57da82 | -3.29102 | -53.83275 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fba8c8aa-0953-35bb-ab8f-3ff07a475718 | -5.00578 | -44.79749 | 2024-11-21 04:31:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c099cb2c-9106-321e-9ef3-1da565fd1572 | -5.45176 | -43.23175 | 2024-11-21 04:31:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730ed066-4e30-3ca1-9f14-b195c140fea6 | -4.10452 | -48.48506 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aaaa686b-85b2-337b-b8cd-d6f671eac7ca | -4.06931 | -51.0379 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1faecfa-0ab4-3656-8d47-e7dc8dc706d6 | -5.62355 | -43.95334 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eca3194-0acb-3ca9-aec1-49b729d3c04a | -5.95167 | -44.23934 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 999f3d29-3b0a-3eb9-a971-a8d3d9ca2474 | -5.2116 | -47.04848 | 2024-11-21 04:31:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65422ab1-083a-383e-913f-21318bb46b6a | -3.2684 | -53.83249 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f87f33e-05b1-31e2-90a9-6f6aa2bd935a | -8.58598 | -50.97994 | 2024-11-21 04:31:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f1de4cd-c424-3fd2-80a5-9c411dd21b9b | -3.56792 | -54.68459 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 37f42539-87b2-31fe-8372-f44074c6d338 | -3.30993 | -54.74479 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3fd7b2b-c9db-3ec4-a11b-ae3bdfa1008c | -9.10193 | -43.19115 | 2024-11-21 04:31:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f924eabf-94b3-3f91-942b-590e3ee0c67e | -5.3519 | -43.79456 | 2024-11-21 04:31:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d221e998-ad61-378e-befe-7455409b22de | -3.39568 | -54.55345 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d50ddffe-5fd8-397c-b51d-5185bdb8d434 | -4.10615 | -51.05084 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dce14df-8024-3cf8-89a9-aa1b0921045f | -7.34759 | -46.40046 | 2024-11-21 04:31:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7cb1d36-d65f-3d28-b02c-294e8d5e5648 | -4.22576 | -47.18433 | 2024-11-21 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc0c1634-baf8-3440-99ec-6604bbf3d658 | -3.11141 | -53.70472 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d373044-e4d7-3bc7-91e7-9d3bf0efbdfa | -4.3455 | -46.13675 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e51782a3-aafe-3071-9c78-47497781cda2 | -5.11727 | -46.17851 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f310fcc3-9d87-35bd-8224-2834e041ae1f | -3.5642 | -54.68812 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10dc5726-2f62-32c3-a058-1295727899cc | -4.41076 | -45.9611 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 599c2fd4-5455-335f-b4ef-6f7e06e8093a | -4.43482 | -48.29673 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 162abaa3-376c-3c00-b1b0-0ad9dc84140a | -6.31407 | -49.67707 | 2024-11-21 04:31:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c0b1e00-591f-3b00-89be-87f24c0e8b31 | -3.80161 | -51.26419 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d9c1d6-8b62-3c2c-b4fc-3de689edd505 | -4.01293 | -50.47754 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc1d1842-06cd-3ae1-b93f-20bc826244d7 | -3.63944 | -51.45642 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97359338-5dc6-30cd-ace5-0459fbcc68f1 | -3.28487 | -53.84133 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea967972-7367-3708-9249-35c7e5026744 | -6.14306 | -41.90696 | 2024-11-21 04:31:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1002b03b-0157-3abd-b8e2-96c07efa7e56 | -3.88172 | -52.24156 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 018a5e64-8d48-3ee5-9f16-2df883285c6d | -5.01655 | -45.10838 | 2024-11-21 04:31:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0719c125-cf9f-38b1-9597-25dc84d50726 | -4.38559 | -47.75454 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48f905f2-0cf0-3824-8df3-74eaab6b9f3e | -4.63071 | -49.5482 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc49b30-0088-33bf-a44e-e7e07749655f | -4.12298 | -53.81948 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f61b59b-d9af-33e9-aa19-38acb88dc009 | -4.38283 | -47.77189 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e047d206-c8cd-3b4e-bb94-9c46091fa767 | -4.19423 | -53.49545 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4c23e80-7b81-3aee-9cac-93d8d1eb5167 | -3.3867 | -53.26842 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b963d725-d587-3aaf-9f9a-0f0a46044512 | -5.54426 | -43.90076 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c97a8536-9850-3f55-969b-8db831aff823 | -9.9941 | -55.65408 | 2024-11-21 04:31:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69532a63-917f-3f41-aa5c-2370d635b78e | -3.37887 | -52.45369 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3391a9c4-67a1-353c-b731-6939cac9edc5 | -3.28982 | -53.84529 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d6a73da-a0c7-3ba7-814d-b789208af884 | -10.73133 | -49.52006 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 021220ea-702d-36c2-925d-be142235f3f7 | -4.0676 | -50.90398 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 921e0a0c-94f6-3a36-8710-e832c09e4c16 | -4.59802 | -47.03335 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ffe8da6-3a13-322a-aba6-94c62d8c0c2f | -4.63245 | -46.42226 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394d59e1-643a-3f8c-8a78-313519d0e18f | -4.42901 | -45.62064 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fda528ee-82f1-3931-a533-805145a031ae | -5.10576 | -43.17253 | 2024-11-21 04:31:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README43.md)
