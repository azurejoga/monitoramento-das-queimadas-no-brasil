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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bb6a093-4396-3e99-a5f0-5f501cae2e07 | -6.51989 | -60.03619 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d926e5c5-c542-314a-abbc-bc0d4a64f8e3 | -6.5191 | -60.04089 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a7ae04b0-c044-3caa-93fd-43a1c094060b | -6.51695 | -60.03836 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40099c8b-a574-3cee-9373-c29d806aa390 | -6.5162 | -60.04305 | 2024-10-25 05:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94b7cc2f-5feb-3f76-a1c4-a5a553c5f5be | -1.44827 | -60.32146 | 2024-10-25 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4063500-6efc-3866-bd5a-24a34b448589 | -1.44407 | -60.32076 | 2024-10-25 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9711fae3-928d-33ad-9354-653a31bbd1c6 | -1.41732 | -60.40813 | 2024-10-25 05:01:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741b6f30-1e92-35b3-af99-2143f105a9e0 | -4.51812 | -61.14068 | 2024-10-25 05:01:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35975078-0304-30b1-90c0-96060723f45a | -4.51746 | -61.1446 | 2024-10-25 05:01:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09c3d7bd-28b8-3ca9-af03-9150b6ef8713 | -4.51389 | -61.13997 | 2024-10-25 05:01:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e454fa08-20e1-3a38-aebd-00416be4a0c5 | -4.51324 | -61.14388 | 2024-10-25 05:01:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10941ffc-3e58-3d97-9aea-97fe1cbf3861 | -3.03571 | -61.67196 | 2024-10-25 05:01:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdfe2062-f2f5-3914-a4bb-8feced1c621f | -3.01257 | -61.70042 | 2024-10-25 05:01:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2f31596-883d-314f-8724-9ec4ce119969 | -2.98751 | -61.44421 | 2024-10-25 05:01:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5953d54d-2d63-3fbb-9707-26f1e40c5987 | -0.76679 | -62.88877 | 2024-10-25 05:01:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79d08d64-bde5-397b-962e-fd479329a4f1 | -0.77233 | -62.88665 | 2024-10-25 05:01:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec2acec-1ada-3178-a06d-197b75ed2381 | -3.7112 | -54.40316 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c58fae89-141c-3db3-89fe-1568572da96b | -8.99765 | -67.03371 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5acbfb2-9281-35c4-8f31-8b6724c86160 | -8.99684 | -67.03796 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66557735-87a7-3da4-9752-66d6bc229d52 | -8.92013 | -67.186 | 2024-10-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a841cf05-e34b-31ae-9d58-07c583b87014 | -8.9193 | -67.19032 | 2024-10-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ac845bc-3444-3e90-803a-1f2a8b1f7b84 | -8.91582 | -67.18719 | 2024-10-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c658bbe-f26c-325a-9840-582ce5ca1e56 | -8.91502 | -67.1915 | 2024-10-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fb1b2f6-20e7-392d-8f56-4ca6d2f139b1 | -9.43805 | -67.14407 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5b30c0c-43e0-3fa6-8189-98ac0949a1f7 | -9.43725 | -67.14835 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72d52a45-a759-3d59-937a-91edaade8ade | -15.261 | -43.63574 | 2024-10-25 05:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 436c54c7-2d48-30b2-b0e7-c710490702b1 | -10.58589 | -44.28868 | 2024-10-25 05:04:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 142a8830-ec64-34a9-9fa7-0e59a3524d91 | -10.57932 | -44.28793 | 2024-10-25 05:04:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d68992be-fac8-3cc3-8a7c-5da6545487e4 | -12.30262 | -43.56717 | 2024-10-25 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5288a77-cb51-3338-a672-cae652608be0 | -12.3019 | -43.57389 | 2024-10-25 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e22e1bfc-b9f7-3f36-bfe4-affd67a0ab2a | -11.78434 | -43.76669 | 2024-10-25 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d12d6201-6fcc-301f-b22b-ab1355c8fe64 | -11.57973 | -43.97852 | 2024-10-25 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bb2ae1fc-8d1b-3552-8e25-fcbfb7bc944b | -11.57906 | -43.98469 | 2024-10-25 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 96641238-24c1-34ab-9606-881565ed712a | -11.57775 | -43.97792 | 2024-10-25 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6fcdc141-fc54-382a-a779-bbe04e06e6af | -11.57704 | -43.98406 | 2024-10-25 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11c9c454-ae11-3dba-a5cd-089085b50b0d | -13.28837 | -43.96563 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7af31c7f-371a-33c4-b41f-5eeb5c68b60d | -12.58181 | -43.836 | 2024-10-25 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 24089b66-32e7-33a2-8c7d-9945b85e728f | -12.5817 | -43.83431 | 2024-10-25 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2cd624c9-73ba-3c06-9e30-314a0baa8232 | -12.58113 | -43.84238 | 2024-10-25 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eeac281f-acbf-3f0e-ab85-831618b57184 | -12.58099 | -43.84067 | 2024-10-25 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15e50b3c-dff8-359e-aebd-699c1180a20e | -12.44211 | -44.4085 | 2024-10-25 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24253321-f1cb-3aa9-b125-641447b7bf86 | -12.44146 | -44.41436 | 2024-10-25 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca54bbc3-8b38-3a67-8950-b1a77af2f171 | -14.11981 | -44.30986 | 2024-10-25 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a9631112-c014-33ae-be24-4974f32eee46 | -14.11916 | -44.31622 | 2024-10-25 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 01512141-8f62-3dc8-a49e-17886350a0b4 | -14.11875 | -44.30952 | 2024-10-25 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 516bed34-474e-3f96-96a8-40c25355dfb4 | -14.11806 | -44.31588 | 2024-10-25 05:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3bb94e18-cb47-3aeb-a36e-da193a822973 | -10.8707 | -44.78718 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a07717c9-1299-3aa5-ba81-b322366db661 | -10.87008 | -44.79259 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02728575-9c88-3bea-9a40-57e0bfcf00c8 | -10.86947 | -44.79791 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eaf31ca-e0e9-3fb8-a207-d01a6d01cb43 | -10.86861 | -44.79102 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d41244f-422b-302c-9c5e-1cf057751576 | -10.86796 | -44.79633 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73275f8e-b02a-315b-8161-4dd212778bd7 | -10.86369 | -44.79177 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8d3269c-38b1-3ae0-bcab-971f4df76ed7 | -13.55446 | -46.52732 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32a110a-ddb2-3e58-b701-2866510fc89a | -12.90197 | -45.0741 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e25dd560-7c8a-3ac4-be09-11addd948b01 | -12.90137 | -45.07949 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1320d2-7292-3fd3-ae36-c1da16e8dc74 | -12.90077 | -45.08488 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2228f16-9be8-3ac8-8dc2-8d6301664bfc | -12.89553 | -45.07334 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6471fdd4-9eea-33eb-9aab-1786d64f4c26 | -12.89493 | -45.07873 | 2024-10-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56e10627-b04b-3893-84a1-7c91517b47d9 | -9.27238 | -46.22209 | 2024-10-25 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bf35da2-dcc8-346e-ae5e-026775a0e3c0 | -9.26665 | -46.22145 | 2024-10-25 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44cf8690-df02-369a-ab1c-1286f387b7fd | -9.14608 | -47.1057 | 2024-10-25 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c740adf6-644d-368c-a656-81a65f7fb2f1 | -9.14563 | -47.10912 | 2024-10-25 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 732b610c-c8b2-333c-b6da-d0564a862da1 | -9.1407 | -47.10495 | 2024-10-25 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 954b0d24-b8b5-3bc4-89d1-b1cea833215b | -9.53103 | -46.69479 | 2024-10-25 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4d93473-f3a3-3e1d-8ba2-78bc682778af | -9.53055 | -46.69854 | 2024-10-25 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe8b599-8aee-3474-bdbf-6c09016a6947 | -10.46023 | -47.3353 | 2024-10-25 05:04:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b16dee-a0e8-3b67-9dc4-10419ecdb98e | -11.93333 | -46.58415 | 2024-10-25 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f190a984-0528-392d-8e06-88bf98e8a873 | -11.93285 | -46.58802 | 2024-10-25 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d585197a-7dba-339f-adf6-f8868bf5001c | -11.69108 | -47.12661 | 2024-10-25 05:04:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4eb52d29-53cf-33f6-aaf3-72a4dd0ff28f | -11.69062 | -47.13035 | 2024-10-25 05:04:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49b30217-2684-380c-ad07-6772be96c796 | -11.19436 | -47.56633 | 2024-10-25 05:04:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a804fe0-8b0c-38f8-aa9f-da76e6acce2e | -11.19395 | -47.56966 | 2024-10-25 05:04:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a05b6611-0e3c-3443-9c5d-82c64722b39c | -12.56275 | -47.04867 | 2024-10-25 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 447aa7cb-572d-3f5c-ad52-a76ccb8443c2 | -12.56233 | -47.05223 | 2024-10-25 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3dca846-94a7-33aa-8a09-4dc00a7e5263 | -9.26887 | -47.91409 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad246c53-4a11-3df2-834e-cc127077dd1d | -9.26375 | -47.91345 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d6c9b36-89db-300b-9794-455b7be7db3f | -9.07492 | -47.9939 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87ee900d-8037-3f08-9cc3-0b5c7eb45b3c | -9.07452 | -47.99685 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c9ddbfc-37ea-3560-b89f-c754a09f4163 | -9.07411 | -47.99978 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3d99dbe-ba8e-3732-ba4f-be100f2a76b1 | -9.06864 | -48.00211 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad547249-df3f-345a-9d60-a2ecfdf23d09 | -9.06823 | -48.00508 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e326eb2e-5f14-3f37-aa3b-fb42704baba3 | -9.04671 | -47.81818 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9311a25-70cd-30ef-8d12-6cd6a0a37c83 | -9.0463 | -47.82125 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dba85f3-7ba8-38da-aa81-299533b5998b | -9.04117 | -47.82061 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4993f30e-2d76-3e5e-a275-9f435afe39c7 | -9.01563 | -47.76016 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2b80b9c-a7aa-3bf2-9253-4a1c05edc7b3 | -8.9585 | -47.63787 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e66c571-c862-346a-a966-caed77d05564 | -8.95809 | -47.64101 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9195434-6b97-323c-a4a2-fccd4c3621b5 | -8.95291 | -47.64027 | 2024-10-25 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1575ee6-d8c7-3282-89fb-e8e88b723557 | -8.9525 | -47.64341 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb058408-9268-3990-95e5-0e28552eed85 | -8.91045 | -47.72351 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb59ae0-4bca-30fc-851e-9195232bd7b0 | -8.91005 | -47.7266 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56389e93-4e93-3a75-88e8-23e03f4db65b | -8.90795 | -47.72505 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c228c0-89ec-3c82-8b25-2744f445037f | -8.82166 | -47.93879 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94ae83e8-aca1-3844-82dd-262c68d4c02b | -8.81658 | -47.93812 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb22dc6f-b3b4-3ece-919b-c941636d8791 | -8.81151 | -47.93744 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a76c28-243f-3a62-80be-7def920346ab | -9.27825 | -48.26447 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe6eb1f0-ad54-3392-8a01-1197dd8073ac | -9.27789 | -48.26273 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ab19fe3-5949-384d-9f90-89b017f37511 | -9.27325 | -48.26384 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c5b01f-d9c1-36a3-a241-1e4acbaf693e | -9.27289 | -48.26213 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ad343a-93f5-3075-812a-bb9d3444017e | -9.25025 | -48.32366 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README96.md)
