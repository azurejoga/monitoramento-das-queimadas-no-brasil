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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3e02c3-1619-359e-b43d-62f6b6e7ef83 | -5.09105 | -47.4846 | 2025-10-08 04:38:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d8b1b3a-d245-3b9d-b32f-a2617bba8a38 | -8.15897 | -50.16241 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 228f9af3-ceda-3eb8-9218-5237a100894e | -9.18542 | -47.7965 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5cea3ae3-fdac-350c-ac27-27c78bd72006 | -4.40266 | -49.7685 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00ffea93-2734-3b61-ac02-82164eca8233 | -9.03663 | -49.76817 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff82f1b-3d29-3fac-9c4b-fed33e96f89f | -8.68064 | -44.73577 | 2025-10-08 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bdc98ae-a6d4-3174-97cb-a2ba02c2816a | -8.27087 | -47.0085 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48df5e62-c3b7-39dc-b18f-658bbdc01b82 | -10.94192 | -49.48099 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b644f28e-f964-3d9e-9b8a-7ee8eb381dfd | -4.40044 | -49.76098 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d673abb9-3ff8-3228-b048-725453c5b723 | -5.1744 | -45.13487 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4210aef2-4c1c-3e06-85e5-8f13d7d5c097 | -9.00627 | -47.50005 | 2025-10-08 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a5a9489-d663-3875-bca4-89d2dcfafc11 | -8.51904 | -46.28461 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd51f638-ba6d-3951-ae57-3665222ce151 | -10.33911 | -48.15067 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6174ad51-424f-3612-ac08-71213aaf2252 | -8.21803 | -44.20292 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de6f853d-574c-3ecb-b7b8-e88515f97f09 | -8.51808 | -46.23999 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdb582e5-c299-32f1-998e-65e8b06110e7 | -11.03103 | -50.88192 | 2025-10-08 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12f111e1-2def-31fc-a96a-290dd7e8a261 | -5.16485 | -46.22795 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8dfb16-7548-3fd6-9a8f-7ab24609140d | -8.48171 | -54.94537 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 440e3be5-f147-35e4-b115-2e250230ee74 | -11.05886 | -47.92994 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd06f64-e7d2-3952-804f-ba05313eef2b | -9.02268 | -45.79948 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7051f6be-e88c-385d-994b-7b61d7a888ba | -4.2604 | -48.26118 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35ddf316-fcef-38bf-90ee-7b2caf53a314 | -9.19199 | -46.91173 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d994fc30-b472-320a-aa96-7df55ab896de | -10.35419 | -50.28653 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cce16e22-25e2-3b2b-bd10-29924de6fb3d | -5.3649 | -41.0041 | 2025-10-08 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5992900d-9ccd-33b2-95ee-b8055db8eaf0 | -7.24527 | -44.15292 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6234676e-8f19-372c-9a56-846697929bb5 | -5.3029 | -43.05575 | 2025-10-08 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 34bad791-b11f-3cec-9fb8-5dbf5986b22a | -9.02199 | -45.80418 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebab6a37-f0fb-3bc0-af03-b7856b208ec0 | -8.41062 | -46.80346 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03a6f155-8849-36ce-b617-515b0b86f7a3 | -12.5109 | -54.714 | 2025-10-08 04:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a6cce294-9657-3538-8084-35614db9463d | -15.14886 | -52.76189 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4da8f0df-74fb-3fad-8a3f-220299fc29aa | -12.39123 | -51.1296 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05eae662-38b5-3d72-8ddc-474f04a04354 | -17.13905 | -45.78631 | 2025-10-08 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a66e67ae-ed8a-3f0d-aaaa-7e8aa33e5f75 | -13.39502 | -46.70191 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7d06d2c-39cd-383e-a4de-f720fef33ad0 | -13.29104 | -48.47393 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69e1faaf-176b-38a7-9382-cdf0c24889f6 | -15.26016 | -46.34535 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 606460b2-6ea3-3fe1-9011-96522835cae4 | -15.31151 | -46.15572 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0d346a5-2a27-311f-8143-83aa20f8507d | -12.64103 | -50.5598 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d8991cae-f90e-38e2-a3d2-ae84887861b9 | -17.29044 | -42.64941 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cfe28b4-78a9-32ff-9094-b17fcc9d5311 | -13.73664 | -45.72501 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d770449-80b9-3585-801e-9513cd71d831 | -14.38096 | -46.01799 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 710071b0-5184-3c80-ba17-398d853fcdc8 | -11.74298 | -50.93328 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eff3db67-653c-3de8-b346-82e16957f65a | -14.95886 | -46.82197 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2955d6e7-b518-31d0-b63c-5008d84ab6e0 | -15.37505 | -47.32536 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e20d41c7-0c1a-35d1-895f-935cbd13ce98 | -11.68046 | -50.96277 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fdead65b-c503-3bca-889a-e76f83afc701 | -15.4019 | -48.01937 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35a24e61-a696-32b6-8913-57a3f74b705d | -15.26552 | -46.33593 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cbca379-389e-38ff-ae68-a721c67e5c91 | -18.40471 | -45.20967 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d7b831c-2446-304e-9fb9-191360c20573 | -15.59687 | -47.25517 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfb92911-d984-3260-a341-4ebe535044c0 | -14.91735 | -46.80876 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c095b298-53c9-3e0c-a30d-2fc0ee87b891 | -12.13674 | -45.59457 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ddfd71a-aeb2-3b64-9501-86026a7012f8 | -14.64751 | -52.54434 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c38083ca-a44b-3c3a-9416-995a08c05143 | -11.6799 | -50.9663 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69ecaba4-658a-3802-83f1-4e82172947d7 | -11.44391 | -50.20374 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93517c2d-3ce1-33ce-bc7a-0ccf9a9d7c57 | -11.14931 | -54.88048 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d8c5470-eb8c-32e8-9784-8a0b568d3e09 | -15.99597 | -50.96871 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 798bfefa-4766-32d5-a211-6b941dcbc7b4 | -13.03291 | -47.91776 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 123bc80f-db70-31bf-99f6-57401b161a33 | -12.39561 | -51.14483 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db141fb8-dfce-3bdb-857a-3d33fd8c56c0 | -12.71484 | -44.37474 | 2025-10-08 04:40:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4082b9b1-a46f-365e-991b-de30bfca7482 | -14.71522 | -46.02819 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1344b226-579c-3ea4-8fe2-6dbc244a61ac | -15.66518 | -43.65379 | 2025-10-08 04:40:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03a445f1-2b81-37de-90ca-7ee2dc2c5d1f | -11.18804 | -54.88742 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60edf6f5-c795-3779-aff1-7f5aaf76ccdd | -15.24601 | -46.35966 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a239c12-26a5-333a-956d-7b6df4489dcf | -11.16607 | -54.89886 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4ae53391-d331-3a33-be60-dce8a399486a | -16.90392 | -53.12808 | 2025-10-08 04:40:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1fd5372-df7f-3860-8668-4b0307a4296b | -13.02636 | -47.91286 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62570069-e2bc-33ba-ba62-2aa072d53d00 | -17.2744 | -42.6503 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ec112a0a-d555-3d08-8288-08eda4883654 | -12.92355 | -54.71664 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1729956-8f09-3cc5-9b66-2520e6211887 | -18.49611 | -42.90517 | 2025-10-08 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f40eb1ce-ae2d-3f5a-9a59-e0c892520fcf | -17.5576 | -46.07486 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb6547f-5b49-34c1-9cd9-d8727cfe2591 | -15.24532 | -46.36473 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e11eb7a-bb37-3f66-974e-9107e18ffc47 | -11.72529 | -50.93761 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3e015c0a-5349-325f-becd-e540e0bf405d | -16.29455 | -45.24312 | 2025-10-08 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f169a3c-100f-30b9-9962-a80519d1a2b8 | -11.95387 | -51.46198 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc55b5e4-c446-395f-a961-1f7a1b1cb338 | -13.30608 | -48.02716 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3423d8bf-c22d-3532-95dc-a379419c5803 | -11.17211 | -54.86418 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3012af7e-0240-3517-9403-3e5541e786f5 | -15.38382 | -47.31746 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90f4d79a-2379-3be9-b3db-8a217b389fbb | -14.69001 | -48.40996 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4b8251-ba3d-3a80-886c-ada64ac97542 | -11.12731 | -54.89188 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d25637c8-9d7e-33c2-8058-9316b2545ce3 | -15.99158 | -50.95315 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82ab3628-39bc-3c2b-b92a-236d1c1b15bd | -15.94805 | -42.60071 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7db483bf-b8cd-3ab5-8e48-7fb058fabda1 | -17.46028 | -49.11459 | 2025-10-08 04:40:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1adcd59e-1bd8-3dc4-8e11-82fbeed0a362 | -13.20478 | -51.69146 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2e91ea1-8b9e-316a-9817-792ba719c4ee | -11.16995 | -54.89954 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6c94b144-336e-3c43-b5ef-a06efa2d6042 | -18.03382 | -51.15366 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81617bc5-f237-334c-969a-15b71cd70b67 | -15.25408 | -46.36013 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6e36e42-7472-3154-8914-4e1d49fd89f0 | -13.02936 | -47.91724 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d239f0c-1467-38c2-8b8c-489e90f18f23 | -15.24202 | -46.35913 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c78ba47f-ecf7-30dd-8b45-222ca3a9e58c | -11.68653 | -50.96739 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9747610-03f5-35dd-aae0-598887371fe0 | -16.5882 | -46.55406 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b57ff84-2725-3a63-bd34-0ab6a08e4c69 | -13.28523 | -48.48922 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cec335dd-2d9b-360c-9096-e3d9cb511032 | -11.28034 | -49.99073 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 452f52b4-7a92-3982-bc23-d0f25d951005 | -12.21486 | -44.26125 | 2025-10-08 04:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6fed3e68-46bb-36fe-8d5f-9ef35217b76d | -14.87844 | -48.25772 | 2025-10-08 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e23530b-e7e1-3a8c-ab04-caea08db5cbf | -14.39559 | -46.03124 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47d81028-9a50-3285-98c6-d4d81bdfdbaf | -11.71698 | -50.94708 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d9e052ff-b353-3586-b5f5-87046d1c8f3c | -11.7839 | -47.54786 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831cf1e1-2a21-3be9-ba0c-205828a39391 | -13.0703 | -48.00955 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29501afa-4865-3824-afb2-3c9785ad1588 | -15.36704 | -47.29751 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7ce91afe-9616-38f1-8a42-20b646f7ee94 | -15.19418 | -43.73083 | 2025-10-08 04:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73f4702f-39dd-3fb7-b323-c52975e75cb8 | -14.36395 | -45.23233 | 2025-10-08 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README73.md)
