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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4102c1d3-5f9c-3464-b39e-16bb60989fd1 | -18.41719 | -42.20787 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 74910f56-b537-34e8-828b-32aa10477392 | -18.41414 | -42.20271 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b0411065-09b0-302d-a3aa-7a148a16dc81 | -18.09413 | -41.48699 | 2024-10-05 04:17:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39a78185-236c-32d2-a1a4-fa419dac6c6d | -18.03667 | -42.61646 | 2024-10-05 04:17:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3b64834-ebac-378e-9c46-fc81ebb9f8ee | -17.94499 | -41.47653 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0c7c510-56e6-3108-b2bb-3c6b5b821c60 | -17.94118 | -41.4759 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14885ea5-839f-314f-8c21-c474d726acc5 | -17.94056 | -41.48057 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa0cb02c-c8ed-311e-9a70-6e8355158718 | -17.93254 | -40.53986 | 2024-10-05 04:17:00 | NPP-375D | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1b264a5-2699-345e-82cb-a44e972b3fb5 | -17.93207 | -40.54352 | 2024-10-05 04:17:00 | NPP-375D | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8fc27ead-ef38-3ac1-8d58-eb1ee45cb1d9 | -17.92803 | -40.54296 | 2024-10-05 04:17:00 | NPP-375D | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bda67021-7173-31d4-92fb-4498c3064d5f | -17.92727 | -40.5435 | 2024-10-05 04:17:00 | NPP-375D | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ce41f03-491f-313d-b62d-ada4a9931b41 | -17.87555 | -42.68508 | 2024-10-05 04:17:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7f2f7010-856b-3946-9107-d65fcc0c74b9 | -17.87496 | -42.68922 | 2024-10-05 04:17:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2762e7bc-a548-381d-ad4f-e5864bb4abb1 | -17.86065 | -41.42262 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 696e3d6a-708a-3731-98c0-4446fab26873 | -17.85997 | -41.42765 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 901ae6e6-06d0-3246-80c1-bd92ca12bef0 | -17.8568 | -41.42227 | 2024-10-05 04:17:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 018131fc-b162-3d00-9794-9a63cc2214b0 | -17.79835 | -42.22955 | 2024-10-05 04:17:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0a47aae-3565-3571-8bf8-bbff715efe9d | -17.79096 | -42.22901 | 2024-10-05 04:17:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59412f9d-5b43-3028-a9d5-a74d3741bfc8 | -17.78726 | -42.22871 | 2024-10-05 04:17:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7034c107-f693-3436-baeb-0199accd25cb | -17.62671 | -42.01411 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 363860ee-2cc7-34bc-95a6-2004cf8f30a2 | -17.62511 | -42.01185 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1eda4935-0ab9-31aa-af9a-34d0646924c4 | -17.62448 | -42.01633 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8ec7ef80-198d-3389-9910-0ef95d0626a0 | -17.62303 | -42.01352 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d0372cf5-206d-3eaf-8790-8e545da05c0e | -17.62241 | -42.01802 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5c87f1be-bc4a-31c2-9eb2-a6d5064f2b8e | -17.62079 | -42.01576 | 2024-10-05 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d3d5df4e-28c7-383c-8d5c-b32cac4f6b88 | -17.60433 | -40.36787 | 2024-10-05 04:17:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4a605fd-2503-3c1a-9049-88b2dca28034 | -17.18281 | -39.28942 | 2024-10-05 04:17:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b43b6406-ddce-3758-8618-407d93ea1ac3 | -17.06891 | -40.95141 | 2024-10-05 04:17:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06b7ee02-9f23-3404-aa08-2c742a11d098 | -25.19258 | -49.32808 | 2024-10-05 04:17:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca638744-9ef5-38b9-875e-03d7ce7f4bde | -24.95994 | -53.47982 | 2024-10-05 04:17:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fcf1d342-6c20-3d66-9682-3b0891f62739 | -24.839 | -51.94662 | 2024-10-05 04:17:00 | NPP-375D | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93a67962-5e27-3ce7-978d-bd51e32149f9 | -20.93276 | -49.01731 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| df5bceab-018c-3f06-952f-fccf826efca9 | -20.92925 | -49.01661 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f13e028d-f2ab-322c-8fa3-cc28d3fa1d65 | -20.92854 | -49.02078 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b1429b3e-e4bb-31d6-adfc-b8cacfbfe850 | -20.92782 | -49.02495 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3115cbf6-eeb7-36ee-a5f9-63ab70677ec1 | -20.92647 | -49.01175 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7b00317-7cc8-3613-809b-5d30ab63216c | -20.92575 | -49.01592 | 2024-10-05 04:17:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a528d9c0-4a41-3515-807c-bb84d73738dd | -20.63464 | -48.75472 | 2024-10-05 04:17:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e099641-5e53-3cfb-b7c5-03c4209eae0e | -20.57977 | -51.39248 | 2024-10-05 04:17:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 991be4e3-fa06-3dbc-b84f-ab81b386b2eb | -20.57876 | -51.3979 | 2024-10-05 04:17:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 616bf05d-f8f9-3e22-bcc5-7050490d4007 | -20.57479 | -51.39708 | 2024-10-05 04:17:00 | NPP-375D | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 291c0c02-8050-3a0b-a0f6-82d8778ec08f | -20.09241 | -50.16164 | 2024-10-05 04:17:00 | NPP-375D | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b18cba70-ebb0-3c2a-a225-0af2dba8389c | -18.37568 | -48.15364 | 2024-10-05 04:17:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e48790e-53fa-3d86-aa99-9417af6ef736 | -18.05816 | -48.76581 | 2024-10-05 04:17:00 | NPP-375D | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6fd62fff-4ab3-3493-a42a-c311e94b6751 | -17.15719 | -56.96597 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 43d06bf9-1976-3d3a-b4d2-55f681e987f7 | -17.17575 | -57.37341 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9be2698c-6573-3dde-ada0-3a2228b00b78 | -17.17142 | -57.36755 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2eac6383-841d-3eed-8a3c-2dd3acf323f0 | -17.17074 | -57.36703 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bf9b2706-5d20-3cd9-90c2-a2094bf4138d | -17.17038 | -57.37243 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 095bf63d-9a03-331e-a7da-b6caf16f2091 | -17.16966 | -57.3719 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e2644372-9982-3ae1-905b-b58501ea982e | -17.16534 | -57.36604 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| af1a5797-b9f5-36b6-99a1-c27a6269ba3e | -17.16466 | -57.36555 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 299b3eb5-6941-311c-9619-b95204459069 | -17.16315 | -56.96735 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d7154b8b-818e-3868-ad7a-7461bfcb7e22 | -17.15368 | -56.14904 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 17037ac9-0ab6-32e6-8044-b4ebce0d215a | -17.15282 | -56.15311 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 304d65be-f877-34be-9fe1-37f8c6d57b47 | -17.15124 | -56.96456 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 095c109c-efbb-3154-bfab-80e7e2d6a1af | -17.15109 | -56.16127 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 37749575-013d-35ac-89d6-56fe3dbbdbce | -17.15022 | -56.16535 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7237bdfc-e00a-3bf1-9557-36b0ab309d35 | -17.14935 | -56.16945 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 98dba6be-7e32-3c52-8dcd-9bb380bf50b5 | -17.14602 | -57.36644 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6ca0ba56-229d-3ec5-96a0-d5372518841d | -17.14541 | -56.15995 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| af46e831-cd15-3f85-88af-f42ce7c76123 | -17.14311 | -57.37577 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 995888cf-9941-31a2-8f64-ea4657e49713 | -17.14258 | -57.41201 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cb764fe1-d5fb-3603-b6ee-e2d2ac539c95 | -17.14157 | -57.41143 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e490b289-d833-3847-852d-d6e3a6db4ce0 | -17.13888 | -57.36981 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2f751e4f-c979-34f9-a080-3e9c29740be3 | -17.13812 | -57.3694 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8e4d2964-3ffa-3028-bf76-9ade568edc1e | -17.13782 | -57.37471 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2244b03b-6174-30e9-8b0f-ea6e426e49d5 | -17.13702 | -57.37429 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 95ccf4eb-67c9-3756-bc89-d16622825fbf | -17.13648 | -57.41049 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cd0c05d2-ae22-3eed-94c9-1c88853bd5c6 | -17.13547 | -57.40994 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b75069ed-4a86-3fc7-a0ea-5ce6018931f7 | -17.13542 | -57.4154 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e6eeb78f-0fd2-3fcd-95f9-4c62a828b0e8 | -17.13438 | -57.41483 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 2d4c041d-b02d-39d2-9486-41cdc119c544 | -17.13436 | -57.4203 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 66e497dd-8bd3-3ad2-a958-6f342b08a07a | -17.13328 | -57.41971 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 3a9d4d21-e172-387b-8505-976be208115f | -17.13144 | -57.40407 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 53e283b3-6ecd-3f1c-825b-ad3410ae302b | -17.13046 | -57.40355 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8eee7a09-9de0-363a-869d-d895f94c55a0 | -17.13038 | -57.40899 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d902b868-6c8b-3ba0-b6cf-590433501763 | -17.12936 | -57.40845 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| bdc93a9d-db3e-30f0-b9e5-14c08c77027b | -17.12931 | -57.41389 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| cc286093-8b5c-3096-89c1-17b9a40d95b1 | -17.12827 | -57.41335 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 4e6dd2f4-a6d7-3947-83ce-48d4dd92ae09 | -17.12825 | -57.41879 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e522c60a-5abe-3fcd-bab8-ced7f58fe3d6 | -17.12747 | -57.39276 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d2b5b88f-84bd-329b-838b-ad3824069683 | -17.12717 | -57.41823 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| d69457d8-7718-3f71-aeb6-1b087e314a7c | -17.12655 | -57.3923 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2d26b99c-b4e2-3145-8ede-459c4ea45c7a | -17.12641 | -57.39764 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f62ecfa7-0eca-3430-920e-9dffb8d5226a | -17.12546 | -57.39717 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e135fa56-fd2e-3934-a908-f1c57368ef19 | -17.12535 | -57.40256 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5a2dcb69-3e0c-3c1b-b17d-1767f38543eb | -17.12436 | -57.40206 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b3ead030-280a-340e-99a8-891f0158976c | -17.12428 | -57.40747 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| bb8d5bad-5191-3747-aa10-fb7c2633f1c3 | -17.12326 | -57.40696 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 23d99ad0-df8a-3c74-9614-0a4bb6aee8c9 | -17.1232 | -57.4124 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 001960b3-ed5a-39f6-a5a3-47a9ce44cb21 | -17.12243 | -57.38639 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| da39cba9-41df-3426-838b-09920f63b856 | -17.12216 | -57.41188 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| fc533988-520e-333d-9db5-cdca96846cb6 | -17.12214 | -57.4173 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| cc6a822d-0407-3d83-9a5b-3f05c35a9010 | -17.12193 | -56.74713 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 372170e1-1a0b-3290-b878-40d3ab2303d8 | -17.12137 | -57.39127 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 837fd5ff-ba80-3dc2-99af-ac598c2cd275 | -17.12107 | -57.42219 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 26e71e43-ff2e-3cde-bdbf-cebb8efa4dea | -17.12106 | -57.41676 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 3c70fea4-dadc-3b85-8868-9c436d7aeea6 | -17.11924 | -57.40103 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f412634b-6f81-3ec4-a0c8-847bc9cef97c | -17.1171 | -57.41087 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |


[Clique aqui para ver as próximas entradas](README82.md)
