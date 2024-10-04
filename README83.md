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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2745a5c2-f724-3321-9287-ea3d42e91291 | -22.26572 | -51.48399 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5a6ca7b9-3d2e-3336-98e0-ca3aeeed88cf | -22.26489 | -51.4882 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 73e05a9a-a302-3186-941f-62c858a0eda8 | -22.26406 | -51.4924 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c6202e55-bb8b-3ba1-aefb-db55d89a4506 | -22.26151 | -51.4831 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2c04bd35-7200-3cf6-b0b5-5c523e36ef8f | -22.26068 | -51.48734 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8ae75716-2f62-304d-a9b5-782df8082921 | -22.25985 | -51.49153 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| df090070-38ee-34c4-9da5-ecdbf8d6a82a | -22.25903 | -51.4957 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3d08637c-1eb5-335d-ab28-1c726e2349ce | -22.25564 | -51.49067 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 50758a81-6ae1-3023-aad2-6d055e7eb389 | -20.99603 | -51.79394 | 2024-10-04 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8219cb0e-c043-33ef-8389-8947db215a5a | -22.46575 | -51.97302 | 2024-10-04 04:12:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c6d0471a-d2ef-375a-a11b-af574ec74262 | -21.40161 | -48.88109 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559561d6-cf5b-3fca-8846-25de55b7f8dc | -20.50182 | -41.81929 | 2024-10-04 04:12:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d2754b8-a3f1-31bc-9af8-c1a1fd9da656 | -20.44212 | -41.98874 | 2024-10-04 04:12:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9320e7ae-c8d4-3c0a-b455-ab6e5094a995 | -19.51376 | -42.32466 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 638d367b-93a2-3445-a909-fbca8f455163 | -19.51144 | -42.32173 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c72152a-d7bf-342d-a5e3-6b30470fac93 | -19.5109 | -42.32545 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 49ccd9dc-b6c8-3d5e-9d0e-2ef859b07b36 | -19.51086 | -42.32035 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c14547f0-c2fa-3782-b96f-e9999c68fd6e | -19.51036 | -42.32918 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b91da10d-7582-3082-9904-bb3ad11e5ec6 | -19.51031 | -42.32415 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ebec597b-c4aa-383e-83e3-1870f130a0ac | -19.50977 | -42.32788 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6a4ab2e9-763c-3408-8e4d-66aa5a928fbf | -19.50168 | -42.31614 | 2024-10-04 04:12:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ebc2dba-2f8a-3a47-ae10-ebe4c274b044 | -19.42215 | -42.50031 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8c836021-98e5-3ffe-8778-2e1f0ff8a3a1 | -19.32496 | -42.59108 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 3d8edd07-0d8f-3bfd-bf08-ffc4860c7775 | -19.32438 | -42.59504 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| 5e0bb6e3-b0ed-301d-b8e4-d333fc6420fc | -19.32381 | -42.59894 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| f7b36cee-a422-395b-bfb7-fce3b8094738 | -19.32324 | -42.60281 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6d7cb576-e849-3b01-8d58-db1a04ed678e | -19.32155 | -42.59053 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 578c7c0b-3076-3ae6-9d87-32a77811dc4e | -19.32096 | -42.59452 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 44100976-3ecc-3e69-8052-474b71276456 | -19.3204 | -42.59842 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 131349ce-dd3b-32d0-9a06-e3f9de88425c | -19.31983 | -42.60225 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 22cb62eb-5fa3-3d41-ae10-995ab9aaced6 | -19.31873 | -42.58596 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 184cc1ae-4748-30e0-8659-52b679a7fa98 | -19.31756 | -42.59397 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 961dbfe5-c5b7-354d-8ea2-75b99d69caa0 | -19.31531 | -42.58549 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 08ba2fd5-4d45-3763-9e7d-63baa170868e | -19.31472 | -42.58949 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 22d49e0b-6a00-3662-a249-44520c0019b5 | -19.31415 | -42.59342 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c3bdcbe1-addf-3147-b9cb-62f7eed58715 | -19.31302 | -42.60112 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8a149e11-1918-307d-8989-67a9135c8b09 | -19.31189 | -42.585 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 027a53b7-303c-3a07-a6f8-bcf79d823c9b | -19.31131 | -42.58894 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1012dbc2-521e-333a-be5e-c4a2ba87e472 | -19.31074 | -42.59285 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dc6ba358-5249-3453-b62d-50fdf27cc066 | -19.30972 | -42.40668 | 2024-10-04 04:12:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 24ce5a30-0bb3-3866-a555-a3a64897b582 | -19.30791 | -42.58833 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ce87b538-b031-35a6-819f-5a19ef20ef1e | -19.30734 | -42.59224 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4d0d113-298b-349c-be9b-3b02da5d3371 | -19.30567 | -42.57974 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8efa92c-eacd-34a5-9b8c-01aac96758fe | -19.30451 | -42.58771 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d4dbadc6-fbed-3d59-b840-d4c723c6000d | -19.30394 | -42.59163 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 799c4f4d-64a5-3d06-b64c-e37d0a939e45 | -19.30288 | -42.57491 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f78fd61-536b-3c2a-a5f2-2894cbcb6827 | -19.30228 | -42.57903 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3507d6e8-a493-3545-982e-7f743688af74 | -19.29492 | -42.58162 | 2024-10-04 04:12:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f31756dd-092d-3b8d-a05e-0071ca91a3d5 | -19.13909 | -42.5212 | 2024-10-04 04:12:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 76afee67-a764-37ea-b6da-84bd6e30c917 | -18.96738 | -42.57059 | 2024-10-04 04:12:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec08444f-a82a-38b5-90da-4f1d954ccb61 | -18.92447 | -42.01837 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4f42b5ea-1e43-356c-9069-c0e63fab4c93 | -18.9239 | -42.02241 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7ab204f7-863c-3201-a991-c51d0819be24 | -18.92333 | -42.0264 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bb51de7d-65fe-331c-9885-34f6c44e4c78 | -18.921 | -42.01786 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d1a3cadd-6af9-3a5d-a40f-bf263c8f2cd9 | -18.92042 | -42.02194 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3522ce60-ee75-37ea-ab44-f219497047c2 | -18.91986 | -42.0259 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b0d0083d-3455-30e5-ab16-13be3ab0e811 | -18.91929 | -42.02989 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 1d74ce60-fd18-3bff-b3a6-426e6d17770c | -18.91695 | -42.02141 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 2d7e23b1-98d2-3a43-ab37-7663e4457a52 | -18.91639 | -42.02536 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 216f4569-504a-35e3-9450-3835fdf8cada | -18.91582 | -42.02934 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 01c784b4-1c99-3a16-acd8-bbfe49028eac | -18.91463 | -42.01268 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e399d92f-4d27-3fbb-bceb-3e4657515588 | -18.91405 | -42.01679 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a294659-a905-36fd-b2dc-3ca207df770a | -18.91348 | -42.02086 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d9ea503a-9782-3a12-88d8-37a3266afc7d | -18.91059 | -42.01624 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0906b880-7d47-317d-bf01-bb71bf6eecd3 | -18.91001 | -42.02031 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fb0a065a-b443-3123-a629-416b1be9daea | -18.90944 | -42.02429 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 067aeb39-159f-3f3d-a033-638a39f366f7 | -18.90888 | -42.02825 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 7c0837db-8493-3ec2-ba3c-08f84e437059 | -18.90598 | -42.02374 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 07cefd02-9d29-3d31-bec8-1a74adbece34 | -18.90546 | -42.01292 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 565abcf3-fda7-330d-aa0f-7694eee01ad7 | -18.90541 | -42.02771 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1276d311-221a-3351-94c6-888dbf244e87 | -18.90487 | -42.01695 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0aca84c4-c401-3edb-a47f-697f7f3d14ba | -18.90479 | -42.00706 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 312dc133-dae2-3e23-8761-b9083f9ac81c | -18.90421 | -42.01117 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0329a7ad-83cb-3bec-8401-2b105d4c7bb1 | -18.90364 | -42.01521 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f6d6ee1-daef-382b-b026-10719e8943a8 | -18.90318 | -42.0042 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| dc9634b6-538f-32d9-9d58-955ac0ad0864 | -18.90307 | -42.01921 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ebf2f3b9-9750-3b6c-8b5e-061ec60ea217 | -18.90258 | -42.0083 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f3ce07a1-cb3f-34a0-9655-2cdf2094a57d | -18.9014 | -42.01638 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20126a54-53f7-3b3f-924e-1112205ead61 | -18.89735 | -42.01981 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5004f2a7-8cd7-3293-a3c8-851be9a9e8e8 | -18.89389 | -42.01925 | 2024-10-04 04:12:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 244fd373-d15d-3078-b344-15ddc2439791 | -18.86651 | -43.13729 | 2024-10-04 04:12:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b59e019-7ac4-3952-91a5-6ad96b9259a2 | -18.86317 | -43.13668 | 2024-10-04 04:12:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 985ea615-8518-37a3-af78-e7998bc4b2be | -18.8602 | -42.91329 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1a679c5a-ac7e-3acf-96e8-0d848065a618 | -18.85964 | -42.91701 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 61cd2c6c-8d3c-3cbb-9513-b45744d32844 | -18.85739 | -42.909 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dc66b6e6-addc-3fc6-8355-3f143a8eeca3 | -18.85683 | -42.91274 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 06c7b3ee-6084-331c-88dc-b2683e770ce2 | -18.85627 | -42.91645 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6ef0bb15-057f-331f-852e-4e13a0281feb | -18.85457 | -42.90474 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3d14f99a-5d98-302b-bc0f-2333ad1ea66f | -18.85402 | -42.90849 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dea6ecd7-22df-32c3-bf6e-5f735d81e932 | -18.85346 | -42.91221 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9d8d38ab-91cf-3bf0-80e3-e20b1c579e30 | -18.85291 | -42.91593 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c764798-1be9-38fe-9c0b-179dfe056d16 | -18.85065 | -42.90791 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 75a5e862-4dd0-3e1a-a43d-e5ff4e88cf68 | -18.85009 | -42.9117 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 71386d1c-ab56-3dc4-9c44-ead58750da1c | -18.84729 | -42.90731 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| b5ce050f-6c14-3eb4-8c88-dbca8e31f801 | -18.84672 | -42.91117 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1f149ed3-3d44-3305-9538-468e61b1f64f | -18.84394 | -42.90669 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 83fd902b-d0b9-38af-861a-a65485c8444d | -18.84336 | -42.91056 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d108dfd3-eaca-3ce2-9c64-bbd9f28b74dd | -18.84279 | -42.91436 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 27eed09a-20e9-3ff4-b6b5-30c5ed65763b | -18.84 | -42.90993 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b1dd6ad9-b8a4-31d0-aecf-cb5b68ec4640 | -18.83943 | -42.91374 | 2024-10-04 04:12:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


[Clique aqui para ver as próximas entradas](README84.md)
