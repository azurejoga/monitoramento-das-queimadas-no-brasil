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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69cd6e3c-ed49-3b7e-80ef-53b3bb3a8858 | -17.90466 | -44.4237 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be94c75e-8033-316d-bfd6-1f842df9a28b | -16.4797 | -45.08155 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74d683fe-e34f-394a-b0f8-a8366ae5ebc8 | -15.74778 | -56.026 | 2025-08-19 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5601db29-945f-3624-89ef-b5e88c22eac7 | -17.33883 | -47.16479 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52bd112b-322f-3833-b138-b62bfc84ca54 | -14.97958 | -54.8117 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 877723ba-f251-338d-a18c-7ac704ec1c82 | -17.42347 | -46.70817 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 477f3c46-8a33-3b24-a046-1525b4d0f4e8 | -17.28742 | -44.88991 | 2025-08-19 04:29:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c446ed2-6c91-3f70-819e-10c8027e0d79 | -19.68205 | -43.26431 | 2025-08-19 04:29:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d1c3930-11d3-3039-b939-70f4c86324f6 | -16.47714 | -45.09965 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2938a9ec-331e-33fe-bf31-f45c1ea44d63 | -21.31763 | -48.6762 | 2025-08-19 04:29:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2def4ca0-5eec-3e37-94c3-d8af22fbd9ce | -15.79573 | -48.22876 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47e8a6f1-7f1d-3e3c-a156-d1369595a921 | -16.01284 | -47.78778 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95015098-00c9-308f-a496-1c9062b9437f | -17.8167 | -44.48222 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92351f22-0ab4-322c-9dd3-3b7461a57104 | -21.23892 | -49.08759 | 2025-08-19 04:29:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 583ecfa7-ed77-32f9-b532-bbd6e88e0949 | -15.02262 | -54.80434 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b754b771-8058-3dbb-8ae8-15a3f7827b12 | -16.15851 | -46.4566 | 2025-08-19 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2790a3f-b9c3-3990-97d4-2c7c4af322af | -15.20027 | -48.75495 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dbee2f8-5eaa-3651-96b5-69d78e84b57d | -16.47778 | -45.08799 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0624382-f623-3b38-b0ec-00209f7f5446 | -17.5704 | -44.47342 | 2025-08-19 04:29:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40628a47-fb04-3dfc-a2ee-4932dba824e7 | -18.43014 | -49.16988 | 2025-08-19 04:29:00 | NOAA-21 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea2220ce-af1a-313a-b83b-ac7faa63494f | -16.48824 | -45.09418 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67d2f46b-daa1-3102-87a5-74ec1f2c61ea | -6.9527 | -43.585 | 2025-08-19 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 67314f22-8636-32c0-bc08-94f47c7840a1 | -6.9336 | -43.6101 | 2025-08-19 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3fca3deb-80b4-3a7b-8406-ceaee442a9ee | -6.9339 | -43.5868 | 2025-08-19 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a46a850b-20ef-3c19-9839-46003f9463c1 | -6.9524 | -43.6083 | 2025-08-19 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1c2ba0f0-6238-3c48-bd50-bee2f5ea5b4c | -6.9715 | -43.5833 | 2025-08-19 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a30cf5cc-1baa-371c-b35d-4c38f3fa1025 | -20.55278 | -54.58002 | 2025-08-19 04:32:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0406565d-d740-3a00-8923-85f66b836571 | -21.87264 | -48.20787 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1adb0b47-b082-3fdf-86ce-13b100bbb017 | -21.98236 | -50.34803 | 2025-08-19 04:32:00 | NOAA-21 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe42d936-41fc-3fd5-971c-06fec8ba9659 | -23.18988 | -52.01259 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 84348b92-a539-3eb7-ba30-357b170985f0 | -20.88166 | -54.98486 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7754c995-3135-32f9-a660-b50ea64d2cf0 | -20.85979 | -56.93695 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0e0fd5a-103d-3909-9c2f-081f1047c978 | -24.04965 | -48.56508 | 2025-08-19 04:32:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9f7cff89-928c-3ec6-bc14-63158590f7e7 | -23.19456 | -52.00543 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 3e463c24-2447-3009-8efa-8c2c06b63edf | -20.86102 | -54.9638 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fda5d46-3d51-3353-ae54-3d27f4401f38 | -20.87694 | -54.9665 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5559e68e-a02d-3a74-b2bb-11c31d7646df | -20.8809 | -54.96727 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4896bd-ec51-359d-bbe7-113c01627e9d | -21.87777 | -48.19668 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 983c3ffb-d65c-3332-9205-fe2253f4673e | -22.88208 | -47.49177 | 2025-08-19 04:32:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 271b7b83-0313-3467-8cdb-7c442f696472 | -21.87322 | -48.20391 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1032b3a1-0a85-300f-8251-ed2024d692b6 | -20.86985 | -54.98213 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d69578c-551e-3f35-8469-08827b965c97 | -21.87662 | -48.20456 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 103873bb-5bd0-3e23-b028-2da1bb1b22ae | -25.04267 | -52.6725 | 2025-08-19 04:32:00 | NOAA-21 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46b98e9b-ad7a-3408-9f49-70ef98be94db | -23.18715 | -52.00805 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ba598fa-948f-3075-937b-1c9968921e95 | -21.72115 | -48.19223 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27142a9c-212f-3834-beed-044df5763796 | -23.78534 | -51.70904 | 2025-08-19 04:32:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b3afb987-b3e2-38c7-bf7a-013bd0164540 | -23.37085 | -46.59725 | 2025-08-19 04:32:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a506c354-0c2e-3022-9109-ed5cf3ffbb5d | -20.85882 | -56.94179 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d3df8aa-86d1-3d20-bd82-a49b391dd360 | -20.86308 | -56.89732 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7777e4d5-9969-3757-bfde-1b15323fd699 | -24.24109 | -54.03401 | 2025-08-19 04:32:00 | NOAA-21 | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 385c79f9-7372-34de-a5e4-aa2a4d0b2d24 | -21.87604 | -48.20852 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dacfce54-910d-36d9-8eff-0d61b5c90f74 | -20.86497 | -54.97324 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1330dccb-9d4f-3e73-b129-eff62829f5be | -24.12574 | -48.71737 | 2025-08-19 04:32:00 | NOAA-21 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 28cd914f-af06-3466-815f-e505ff9fb3da | -23.99446 | -48.56035 | 2025-08-19 04:32:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84022889-c4a6-3db8-9d89-788b1a2e90c9 | -20.87879 | -54.97835 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9664b9f1-454d-3991-af83-2d5cb50dbb24 | -20.87099 | -54.98512 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a656c508-1c02-3def-abf0-d72678d3573f | -20.8657 | -56.90744 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbf94b27-0b71-34bf-b395-9bb9573a8f40 | -22.59672 | -54.90965 | 2025-08-19 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b0d8a7f1-7878-3598-933c-e7c19824e2a3 | -25.16031 | -52.25909 | 2025-08-19 04:32:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6901c97f-d9c1-3338-8306-fab690b61aea | -22.11519 | -49.66889 | 2025-08-19 04:32:00 | NOAA-21 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad3cd2f0-2842-3821-9f02-e3d5ed3e80de | -23.19325 | -52.01324 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9340e106-b345-30a8-8c94-48429a4b09e8 | -22.07827 | -48.74186 | 2025-08-19 04:32:00 | NOAA-21 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86d8e925-58d1-3866-9920-dde81fb58e26 | -21.88573 | -48.18998 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34efc19f-7dc4-37a6-80b1-a03bb20bdbec | -23.19118 | -52.00479 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 6d9c9914-0f74-3a1a-8a8d-66c8fc6f60af | -23.19053 | -52.00869 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| d9acfb67-be09-3d35-8820-426c9ebcc93a | -20.88062 | -54.99036 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a828840-a0c9-3b52-b61c-a4c96bedf142 | -21.88558 | -48.19282 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35d49074-4d0b-3c87-8ee1-bea78ff6f971 | -23.07627 | -46.4036 | 2025-08-19 04:32:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6e21922-3634-3e48-a370-0841a5590a0b | -20.8767 | -54.98934 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 751ed05c-d818-3fe6-8874-ca08fc3bae0a | -23.99103 | -48.55976 | 2025-08-19 04:32:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82bed458-3077-36db-ae42-705675e5118b | -21.87453 | -45.53854 | 2025-08-19 04:32:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f7cbcd2-f64e-39c4-8de0-c0b9961fb5de | -21.88956 | -48.18943 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c00ed0a-b552-3758-92c6-664909a37b44 | -21.42537 | -48.72853 | 2025-08-19 04:32:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa13d108-4c98-34cd-a7ef-52d2321787d9 | -20.85806 | -54.96621 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bded3655-badc-3881-aa40-c105d40e5cc8 | -22.26188 | -47.04765 | 2025-08-19 04:32:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07da3ee7-96e0-36b1-ad35-778c5db555be | -23.19728 | -52.00998 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abe4c172-37ae-3edb-b513-df107c47d5c7 | -23.1939 | -52.00933 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| 4bab3d55-a716-3513-8aae-15a143498921 | -22.26031 | -47.04953 | 2025-08-19 04:32:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 634e9b17-9797-3529-8206-b318bc8a6ebb | -21.39635 | -48.57528 | 2025-08-19 04:32:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0455f08-004c-3e1d-8c1f-dc3df0bfd156 | -20.86232 | -56.9476 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1ec9393-7f50-3bc9-b03d-2158381f075b | -21.39119 | -48.57536 | 2025-08-19 04:32:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9d75857-eb50-3fec-abfb-d1c1912e8e7b | -24.8551 | -50.72261 | 2025-08-19 04:32:00 | NOAA-21 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 04bee2fa-1fb8-3db5-a1d5-790794186281 | -23.0769 | -46.39884 | 2025-08-19 04:32:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d98e787e-115a-3298-bb17-3918e6f94fe1 | -20.86685 | -54.9763 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0b3eae7-ecaa-3230-9d7e-6d9458365d6d | -22.27083 | -48.50023 | 2025-08-19 04:32:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a3088b9-8eda-36e7-a80e-771cf4673e17 | -20.86881 | -54.98759 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e331c0f-44ec-3032-bb19-50cc31a5e0a9 | -23.37106 | -51.85009 | 2025-08-19 04:32:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 82d727fd-9afc-3a83-bd2c-39ed21418bd4 | -21.8772 | -48.20062 | 2025-08-19 04:32:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16eabaf0-d3dd-3de4-aed9-1aa0e2448ca1 | -23.30996 | -46.88713 | 2025-08-19 04:32:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b73a9547-68f0-3d46-bb8b-a90dd74d605c | -22.31241 | -48.98822 | 2025-08-19 04:32:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd00074e-207d-3349-bf0c-1d82a4a731d1 | -20.86799 | -54.9791 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36c459dd-e312-3065-9d04-725149df96c6 | -23.18379 | -52.00737 | 2025-08-19 04:32:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4578127f-4760-3f9a-a565-bfa2cf22b1c7 | -20.86998 | -54.99065 | 2025-08-19 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a5d4e4c-0610-3a36-ad0c-3fe43d5b3828 | -20.86212 | -56.90214 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0af4362d-c907-3ed0-9f19-7db5e1e26818 | -21.86725 | -46.55558 | 2025-08-19 04:32:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d1eb0d44-5443-30dc-889f-9ac8bcd55dc2 | -20.86923 | -56.91302 | 2025-08-19 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 567a8a0a-ebd8-3aa7-a5aa-dc0a04e9dbb0 | -23.99388 | -48.5644 | 2025-08-19 04:32:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6302bf5e-59de-337d-9d35-a6b59c2480f1 | -24.12517 | -48.72135 | 2025-08-19 04:32:00 | NOAA-21 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9eb043b8-53f4-37be-96ce-24bd3681da03 | -22.89951 | -45.3877 | 2025-08-19 04:32:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d89138cb-0160-3c32-9a98-f5b8e69bb274 | -23.45901 | -49.25117 | 2025-08-19 04:32:00 | NOAA-21 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
