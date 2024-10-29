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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7a5cd53-4aec-31fc-bd6a-f9ec93829a07 | -12.22851 | -44.68774 | 2024-10-29 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8fec00c5-bb75-3201-889d-584cf14803aa | -12.2249 | -44.68245 | 2024-10-29 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebd2454b-a6ae-3f0a-898b-303ce38a83a8 | -13.66741 | -44.06001 | 2024-10-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 356a9cfb-968e-3278-a67b-fbf457bc7f60 | -13.32197 | -43.76357 | 2024-10-29 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31cfaa1f-b824-32d0-9c5e-5f3f37e19d16 | -13.30162 | -43.57417 | 2024-10-29 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdf24ee3-3712-3be9-b13c-bf5e58a3ecc4 | -13.30098 | -43.5778 | 2024-10-29 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59775aea-585c-318d-ae77-7adbad0d0935 | -13.16894 | -44.05429 | 2024-10-29 03:47:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2d25768-7a50-3365-bfe7-b80de0ef1f52 | -13.16868 | -43.54532 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85084b89-f201-3093-8e39-8e6d9e7ebce6 | -13.01237 | -44.0997 | 2024-10-29 03:47:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c99cf87-3b10-374b-9e32-5e4b7dbbdc1d | -13.00747 | -44.10287 | 2024-10-29 03:47:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a020e5f-42b7-3034-ac15-06399f7c2ff0 | -12.66724 | -43.81953 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7e9a71d-f60d-3ae9-a197-4b2a2fd01eaa | -12.66655 | -43.82336 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39dc258e-2757-3f02-ac2f-a630521d6ba8 | -12.66379 | -43.81493 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a5aed7a-9e03-3d8a-a7d4-fac1b23d0201 | -12.6631 | -43.81876 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3900286-e1a3-314b-bba3-833c685cec6c | -12.66241 | -43.8226 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8adcb44-5693-3c0c-ac6c-e64ec7573eeb | -12.66171 | -43.82644 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07f4cc24-1be2-3655-bc53-583d08b79171 | -12.65827 | -43.82183 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 116ccb21-45bc-312a-9d6c-4b90619ecdc7 | -12.65757 | -43.82566 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fed4e7a-7316-37e8-97d8-f2b4b30ac8be | -12.57973 | -43.39668 | 2024-10-29 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b11de82-c097-334b-a0d4-be5e8363844c | -12.49706 | -43.79387 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d340c4e-431c-3f91-961a-c42fcdc04754 | -12.49224 | -43.79691 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 802772ee-a921-3d0a-8efa-8562bbe41339 | -12.44128 | -43.7366 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 921c453f-52d9-386d-87bd-6b2c5234d481 | -12.43915 | -43.73544 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d5afbf87-a8f3-31c6-a4f4-5e654088ae4e | -12.43715 | -43.73582 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ba7b737-8154-38d8-a577-e5fbb88d8c43 | -12.43302 | -43.73503 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13067498-a444-3d2f-892f-36b8d693e70c | -12.43235 | -43.73886 | 2024-10-29 03:47:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 10b22adc-0864-3b64-92b1-71ebddecf4a6 | -3.426 | -42.98932 | 2024-10-29 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f77b4807-d3c9-3210-af62-166ce158b3e7 | -3.28695 | -43.54316 | 2024-10-29 03:47:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d5c5e9c-c41b-317e-a453-2fcc7458043d | -3.88477 | -43.14433 | 2024-10-29 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa92f9d1-4476-3f1a-b5ce-939b86c57b49 | -3.65168 | -44.1885 | 2024-10-29 03:47:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea67885d-e412-32dd-9674-c638be727666 | -3.65076 | -44.19406 | 2024-10-29 03:47:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25a60d39-944b-3ad2-855b-3728f0f33438 | -4.80307 | -43.78911 | 2024-10-29 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 98389435-d8aa-34c3-8efc-bfc85af3ff3e | -4.07712 | -43.9575 | 2024-10-29 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 44344e62-46f0-32b1-b6f5-5272e6d3b384 | -4.70003 | -44.16729 | 2024-10-29 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c48af7db-b022-31a6-9136-bd8a95ced377 | -4.69518 | -44.16646 | 2024-10-29 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25a4472f-9ce2-3c0f-b431-8e5d81d80d92 | -4.65742 | -44.16332 | 2024-10-29 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 901424b0-6b65-3fd3-8387-2091f253dc2d | -4.65639 | -44.15992 | 2024-10-29 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0ad678a6-96d5-3001-8762-1f7b024de5c3 | -4.65257 | -44.16247 | 2024-10-29 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a44b500c-a0e3-3cd2-957c-7a70f31cbb4f | -4.13584 | -44.20715 | 2024-10-29 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e3fc800-1b2f-3e6f-9c71-3a73f949ce28 | -4.13256 | -44.20782 | 2024-10-29 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97e3270c-6657-3511-8cee-6350f0c73d0e | -4.13162 | -44.21332 | 2024-10-29 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a40845af-f201-3e14-9503-a209e22b6be2 | -4.13003 | -44.21185 | 2024-10-29 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a4651192-77d7-3c6f-893c-8b4216c43041 | -5.28488 | -43.41035 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a68c61c5-04b8-38cb-9bb3-992f074ebece | -5.2803 | -43.40966 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f704f4c0-9144-34df-ad8f-22308c2886be | -5.27573 | -43.40897 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bd04ab5a-d717-3f56-8c0b-fdd5c4c18a1e | -6.25062 | -43.57178 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e263ce21-03b5-3aed-bccc-a70d1f59d49b | -6.24605 | -43.57123 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82e8f4d5-f560-3142-a997-55bb6cdab94f | -6.17921 | -43.79809 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b07353e-fb2f-35f1-a63c-66c511a3e14d | -5.93581 | -43.68188 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90b2daf7-e56c-34dc-8bdb-0cfbe9996d6a | -5.9349 | -43.68385 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60349c3c-7ff0-33b9-959a-084f148ef77a | -5.93121 | -43.68114 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a2c9c94-ccc5-3b43-9d4a-cbac2df5412f | -5.93112 | -43.6784 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| abc78cd0-97bd-3dff-a999-01ffe5555439 | -5.93042 | -43.68589 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1058abf1-5e38-3f76-a111-eb2c2518f5f6 | -5.93029 | -43.68311 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b43020ff-5aee-31b5-b4f9-d3b8cf125b6a | -5.92946 | -43.68787 | 2024-10-29 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd034cab-5849-314f-9629-56a31eb0b6fb | -5.73628 | -43.88406 | 2024-10-29 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 79db3352-008a-3a1b-82c4-24bff4c89960 | -5.44917 | -43.57987 | 2024-10-29 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9183c31c-58c8-30a2-a17f-331efd58774d | -5.28409 | -43.41504 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 086c073d-30cf-3c01-a4c1-03c224d2495f | -5.27952 | -43.41433 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b50f1392-b0b1-3a06-9bfb-e05fc82a668a | -6.45522 | -44.67805 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 583b8150-a392-3c8c-9e08-21c9c2fdbc65 | -6.45422 | -44.68377 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c388d2c-54aa-3317-894c-88d256e6a142 | -6.4503 | -44.6775 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 52af1f14-d550-321f-b8c2-cf0471fc444f | -6.44932 | -44.68311 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af5e3615-31d7-3bda-b42b-44a7e7920e8d | -6.19091 | -44.53342 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08d913a8-7ddb-37b9-a251-ec7d6a6e408e | -6.18997 | -44.53895 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6979f179-01cd-3c5c-b777-475d58fe73a3 | -6.12697 | -44.30258 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e0bcc70-cb7c-32da-b535-126b849323e2 | -6.12646 | -44.70348 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9abdaad-a081-397e-a81e-40a12b4d6283 | -6.07236 | -44.62365 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 32b272ae-f82d-398e-9760-9c70cb65f5c8 | -6.0714 | -44.62929 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4cfe8aea-2646-3e5a-9297-bfdd61bbea79 | -6.06747 | -44.62277 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1063ca6c-cdc1-3693-be79-ca94661af433 | -6.06652 | -44.62837 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3b9bf79b-20e8-30cd-a29e-60a72ca9a272 | -6.06163 | -44.62749 | 2024-10-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bceba3b7-71b2-34d8-a219-63f92529d8e7 | -5.92002 | -44.67617 | 2024-10-29 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f05623c-8cd2-33f3-bd9d-993b8727bb24 | -5.90119 | -44.63884 | 2024-10-29 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5906d0a-92ae-3681-8b08-789566832883 | -5.89861 | -44.64209 | 2024-10-29 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d7414e5-ac74-37ae-9cdf-87d9d6319a98 | -5.83998 | -44.68951 | 2024-10-29 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67d13e12-d9b4-3687-b899-6a2584c3679f | -5.06071 | -44.21624 | 2024-10-29 03:47:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4defc8ad-eb14-32bf-9684-50a2998cd707 | -5.05982 | -44.22155 | 2024-10-29 03:47:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9cd414b4-ff9f-3097-952f-e3368f1bb63e | -5.05411 | -44.2259 | 2024-10-29 03:47:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2690214-c95e-3aff-86c6-ea2b8be9253e | -5.055 | -44.22062 | 2024-10-29 03:47:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cacef99e-dcf4-399d-94db-0d3c90e5f274 | -7.25555 | -44.1977 | 2024-10-29 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c97eaa8-4c0f-3ab4-9255-0253f22e4dbb | -7.24913 | -44.01205 | 2024-10-29 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aee9247-028f-3f7b-b870-4739122a50d3 | -10.87123 | -44.53838 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b06eb72-903b-32bf-b6b1-ebae992b28dd | -10.87042 | -44.54299 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48c062a5-9092-3eaf-b6e4-ad5cd70a1f81 | -10.73984 | -44.56354 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3af97e21-5194-3f11-a2a7-12e39308c2b7 | -10.54273 | -45.14085 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c3b698de-2dee-37d6-b1bf-d3e187e429d3 | -10.51905 | -44.84697 | 2024-10-29 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 734d8dcc-06bb-35b2-8454-022d01920aaa | -10.51816 | -44.85186 | 2024-10-29 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcf091ee-1350-3974-95b9-462fbb3ef36d | -10.51479 | -44.84919 | 2024-10-29 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3c543a8a-8e86-3254-988c-64a8e87fd7a1 | -10.51446 | -44.84612 | 2024-10-29 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f72104b-133d-3773-a7c0-cbba59fde408 | -10.51356 | -44.85104 | 2024-10-29 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 465e4ae6-9241-3edc-ae8c-abc7dd57788c | -10.4895 | -44.59351 | 2024-10-29 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4780ae3c-1014-3a59-9164-732d39ca92f7 | -10.48498 | -44.59264 | 2024-10-29 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 397586dc-d325-3546-b00b-c461e5221e75 | -10.48414 | -44.59733 | 2024-10-29 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8084d99d-a526-3ac5-89ce-ade1b554bb37 | -10.44924 | -44.89668 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7a7aacb6-08d6-385c-9018-d884c91c2e5e | -10.35581 | -45.09312 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8db8796d-4a9e-3860-bde3-0a030372a0b8 | -10.35114 | -45.09216 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 708bffaf-3527-3735-9f45-0effaf6ba7c1 | -9.85856 | -44.32443 | 2024-10-29 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9c65117d-532d-3c96-987c-0c92277267b5 | -9.85408 | -44.32358 | 2024-10-29 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1ca82a44-49e9-3cea-be67-e5d24ff014a4 | -11.40594 | -45.13822 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
