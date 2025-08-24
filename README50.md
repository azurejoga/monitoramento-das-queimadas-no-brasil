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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7502ef8e-5fbf-3d26-a348-5e6a8e630813 | -23.31356 | -45.53092 | 2025-08-24 04:38:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 9fd54932-2da8-3989-a483-0d605981c0cf | -20.35929 | -51.68254 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82be5f2f-eb20-3c98-b5a4-ff1bf35c5a5f | -20.28547 | -50.89345 | 2025-08-24 04:38:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 884c7661-847f-3f26-a89f-d7e7bc68eb2c | -22.45838 | -49.00683 | 2025-08-24 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3894846-c888-3fda-af24-c6938e165ba6 | -23.56793 | -51.4441 | 2025-08-24 04:38:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c4368c1f-6a70-3479-a750-19380f123299 | -20.36202 | -51.68681 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5878b74e-3f1f-3b51-8d22-307308add009 | -20.29097 | -50.90194 | 2025-08-24 04:38:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ca00b59-3593-3b28-9682-0fd20f275843 | -22.94807 | -45.12984 | 2025-08-24 04:38:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 34017794-e383-3cd8-93bc-3a2b3e8ebd3a | -20.28766 | -50.90137 | 2025-08-24 04:38:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4c30ce36-98ec-3ebc-80b4-45cb8cab766e | -20.9459 | -46.83317 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890ef472-ad4f-32c3-99b9-d695db8d3a0f | -22.71869 | -46.98056 | 2025-08-24 04:38:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| afbfe4b9-d5e3-38dc-80bd-979e97183021 | -23.10621 | -49.98758 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| daf1caa7-f103-38da-9f6f-dc59700bcfdd | -23.30829 | -45.53866 | 2025-08-24 04:38:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8695c38d-f2ca-325f-b3d3-c032c4961864 | -20.9453 | -46.83798 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df2caa24-7abb-3dbd-a499-0297718887f6 | -21.27277 | -43.75383 | 2025-08-24 04:38:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e9da084e-9054-3ab7-994c-8921f1492adb | -20.61416 | -51.11974 | 2025-08-24 04:38:00 | NOAA-21 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a81dcd0-fc44-38a7-ad9c-22fc172d9c1b | -22.61113 | -52.49846 | 2025-08-24 04:38:00 | NOAA-21 | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 547d9228-622d-37db-9266-a1c78fcfbc1a | -21.89804 | -48.83247 | 2025-08-24 04:38:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| a33b36c7-e961-3003-9453-b692c0e26ae8 | -22.12602 | -43.24651 | 2025-08-24 04:38:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e0e9ecb-7014-3fba-991c-66ed296b6702 | -20.94651 | -46.8284 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79a584f0-10f4-3a64-a8b2-dad416a5007c | -23.10795 | -49.97556 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9ea7dd8b-b341-387e-b9f1-a455b6720de5 | -20.35034 | -51.69606 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5472ca21-d023-32ed-8390-dd5953a3062a | -20.35209 | -51.68504 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d06674fc-2c5e-3813-a109-f74716782e21 | -22.40809 | -43.42369 | 2025-08-24 04:38:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4b49ac40-664a-3c34-b900-4eed59c2b6b9 | -20.93621 | -46.83564 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9c320c8-5223-3706-a5b2-f222fca860ca | -20.35755 | -51.69357 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7a0bf182-358e-397c-ba3e-f0b9c724b879 | -21.7264 | -46.81287 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1f4b86a8-b9bb-3aeb-b913-ed0f50141b08 | -24.73763 | -48.97939 | 2025-08-24 04:38:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 22cbc83a-6a37-35e0-87be-8d2790a40324 | -21.70248 | -46.90958 | 2025-08-24 04:38:00 | NOAA-21 | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 288abfba-994b-3739-8248-25dcbf6d800e | -20.94398 | -46.83643 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 814658c0-7e8d-38f9-a997-097e41353fec | -20.3554 | -51.68563 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f046a32f-c3df-3e3b-98be-29a1a2239843 | -20.72767 | -49.42723 | 2025-08-24 04:38:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9e70106-aec1-3825-b23a-7c2da341c3bd | -23.473 | -46.8119 | 2025-08-24 04:38:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 05abe2dc-2e55-3002-8319-881ad62c3434 | -23.12155 | -46.847 | 2025-08-24 04:38:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02fe1db8-88b6-3e6c-b7fa-f8a55e918808 | -23.18311 | -49.98717 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5c12f171-2e9d-3dad-ac3e-c8465f81b9de | -20.34255 | -51.70223 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8b528ab6-a671-30d3-9e52-d3fe8af33be9 | -20.3443 | -51.6912 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 38e4c076-0e49-3fca-a90a-116d1ec18bfe | -20.34819 | -51.68812 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c3813392-04c7-31bd-bcf4-fcd692f15a14 | -23.51027 | -47.25662 | 2025-08-24 04:38:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8a6f6273-8fdf-3a32-84b0-16ca0362899e | -23.39772 | -47.00724 | 2025-08-24 04:38:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d916e9f2-775c-3bc7-9543-0b544d2a91d1 | -22.14327 | -43.65217 | 2025-08-24 04:38:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8be87b4c-a12a-37b9-b6c7-b73a9d64f0b5 | -23.94271 | -50.98878 | 2025-08-24 04:38:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d5c185d-e263-3361-870b-2fc960e6d7a7 | -20.94524 | -46.82685 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4856c252-4e5c-3f12-adc9-3d8b2186c7a1 | -20.35813 | -51.6899 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 30947e96-e605-3533-ab64-9790542af9f6 | -20.35092 | -51.69239 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 20cf7158-3c1f-303c-9ace-32b260946f53 | -23.3474 | -46.09401 | 2025-08-24 04:38:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 43f9db90-1cca-38cc-b8fe-f6d52c72b055 | -20.34761 | -51.6918 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e706adf5-4a6e-32ad-a3bb-5d1ff1ad6179 | -23.35484 | -45.80609 | 2025-08-24 04:38:00 | NOAA-21 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| db3cf0af-a6cd-3801-81e6-24d640e8ffb3 | -23.25569 | -46.62546 | 2025-08-24 04:38:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 12f7b09a-bba3-33d6-bc51-251f339f4dbe | -21.89812 | -48.16864 | 2025-08-24 04:38:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41b3630c-f85e-39a7-977f-6bb8b55a0124 | -23.49721 | -47.07367 | 2025-08-24 04:38:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1c52924e-c774-3f71-99a6-260fe10a9e28 | -21.40884 | -47.61349 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 371060ce-a504-366f-89d2-7caddfd9b4ac | -22.7942 | -47.80845 | 2025-08-24 04:38:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 762bdeb2-aea8-38d3-852b-6ca0232e1405 | -20.35482 | -51.6893 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| cdb4989c-697c-3e38-a1ac-a7a3a80b2677 | -23.74069 | -51.40462 | 2025-08-24 04:38:00 | NOAA-21 | RIO BOM | PARANÁ | Brasil | 4122107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a5a4d37-aaa5-32d6-b909-af238d66dd1b | -23.54821 | -47.10999 | 2025-08-24 04:38:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 956b282a-b809-3bd1-a599-15d21745d744 | -23.91219 | -50.50831 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3341d53c-d0af-3d2a-8472-f9d813c3d97a | -22.60781 | -52.49784 | 2025-08-24 04:38:00 | NOAA-21 | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 77455621-8100-3b6f-a0a5-639dfd9ad1d4 | -20.34645 | -51.69914 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 36666a98-bfc8-3179-b35a-9f9e6328e85c | -24.73994 | -48.98967 | 2025-08-24 04:38:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec1cc9df-5f32-3539-adbf-5c323d9c6d45 | -23.49337 | -49.89557 | 2025-08-24 04:38:00 | NOAA-21 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a57cf35-db82-382e-b519-bc3d7c8b9fd2 | -22.79359 | -47.8131 | 2025-08-24 04:38:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8af81c0c-bdaf-3b82-8d2d-f388e5dd83d3 | -20.80638 | -50.12612 | 2025-08-24 04:38:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c104c6a8-961d-3902-a190-d72dec984fdd | -21.86134 | -50.35746 | 2025-08-24 04:38:00 | NOAA-21 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7d92e9b-f88b-384b-888e-3cc877d748f0 | -21.38978 | -43.87757 | 2025-08-24 04:38:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bf9410f8-d35f-3440-b26d-f8abfc47e81b | -22.03603 | -45.0212 | 2025-08-24 04:38:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bbdfd030-bb5f-3d5e-a89f-b07ac482d3e9 | -20.94009 | -46.83607 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b73c3149-a53e-30d6-84a8-19d1b36e5acf | -23.89246 | -48.58295 | 2025-08-24 04:38:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e97c947e-5be0-3283-9591-9e84d2473aca | -23.91318 | -50.50733 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17e3584e-c878-3a24-abd4-88f4f9a22517 | -23.13515 | -47.03165 | 2025-08-24 04:38:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 56eec8f7-f5e7-3000-ac26-10d04813e81d | -21.7017 | -46.90752 | 2025-08-24 04:38:00 | NOAA-21 | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 62d329a0-f496-3a0a-a42d-3ade693a53bb | -22.03603 | -45.01956 | 2025-08-24 04:38:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d0fcf0e0-9621-3344-a3e4-011d2346d5c7 | -22.95197 | -45.13484 | 2025-08-24 04:38:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 288689b4-92a8-39fe-843f-6c075623fea5 | -22.51276 | -46.67701 | 2025-08-24 04:38:00 | NOAA-21 | LINDÓIA | SÃO PAULO | Brasil | 3527009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd0df3fd-9306-3543-8263-7f7c17a600c9 | -22.7881 | -46.71605 | 2025-08-24 04:38:00 | NOAA-21 | TUIUTI | SÃO PAULO | Brasil | 3554953 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 42cd5169-fd36-338c-8ea3-e00441cef883 | -23.25523 | -46.62926 | 2025-08-24 04:38:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1718b548-7bff-3a46-a6b5-9f1b450ba187 | -23.62553 | -46.02671 | 2025-08-24 04:38:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| eb20c87e-cb98-3e9d-a154-148cee5ddc6a | -23.18711 | -49.98375 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4419e55c-6133-32a6-a57b-a727f542444e | -23.32575 | -47.84051 | 2025-08-24 04:38:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 66d64b17-aae5-386f-bf4f-7182262591b0 | -20.80302 | -50.12555 | 2025-08-24 04:38:00 | NOAA-21 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 2ded5d71-c27d-3ddf-9753-8b416c5d5c2b | -23.63234 | -50.55881 | 2025-08-24 04:38:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| aaae6071-3981-3ff6-bac6-4e4aa31c1d92 | -21.41317 | -47.60942 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35aa5d3a-c118-37ad-8610-0038a6f5cc66 | -22.73242 | -46.96665 | 2025-08-24 04:38:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 082eabdd-2700-330c-867c-2bf95a0bcf64 | -23.35156 | -46.09463 | 2025-08-24 04:38:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01e84be7-ba4e-3fbe-b40b-bc06f9a456c7 | -20.94786 | -46.8369 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e11a082c-f63b-3479-954b-993132a29982 | -23.63176 | -50.56274 | 2025-08-24 04:38:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7e6ff877-6a49-3e1e-a1d7-138c4ddbe621 | -23.2791 | -46.56673 | 2025-08-24 04:38:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f35fda0-61cb-3434-9240-2d47c4449a92 | -20.35151 | -51.68871 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8e5a7d16-a09b-328b-a6eb-a1c4ea6c4772 | -21.73032 | -46.8134 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5b590e22-8871-33ab-9007-dade29288405 | -22.72651 | -46.98182 | 2025-08-24 04:38:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 036a3b92-78ea-3d72-9c0a-2c545b110374 | -21.54733 | -44.17178 | 2025-08-24 04:38:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 904bde69-f91f-34e4-94ca-3555f4acf308 | -20.87009 | -55.0036 | 2025-08-24 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d61ace6b-0b06-3bbc-8351-3b802507cc4c | -23.8455 | -50.72662 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4a84397f-d5d6-3269-8495-7e79964098bc | -23.10679 | -49.98357 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bbbef396-bce9-34e8-ad76-bb3cbc733703 | -20.94136 | -46.82645 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1a9c6086-4db6-39d3-8465-d669b72245ec | -22.45779 | -49.01104 | 2025-08-24 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2818a7f7-c4ef-32b1-9e1b-4726dc5357bb | -21.41257 | -47.61408 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2aefb33-4526-345f-8e5d-aa8a364fe57c | -22.22181 | -45.69187 | 2025-08-24 04:38:00 | NOAA-21 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| dbde87bf-866f-3f6d-a6bd-efee889082d4 | -23.1102 | -49.98417 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0ad217d5-811f-33db-b638-18a9b5ef598c | -22.90539 | -47.72323 | 2025-08-24 04:38:00 | NOAA-21 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README51.md)
