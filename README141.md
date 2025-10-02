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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34faab2a-0757-34c4-a28a-e0654bae335c | -12.26474 | -47.81469 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fc52ae2c-37ab-33fe-a942-d22c16047b44 | -13.46257 | -47.22839 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0123681e-ca9f-349b-8ba0-dbdc3b08a81a | -14.47572 | -48.40327 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6bf533fc-14f0-3e22-bb51-8247075a2d24 | -13.43125 | -47.79363 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1efa312d-382e-3380-a7cc-1774fc624455 | -11.86709 | -45.0072 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 77753a18-a6a9-3790-918e-6017a8579b52 | -13.37056 | -47.28193 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a3bcdaa-66b8-3588-801e-ff3b339cc90d | -15.99909 | -50.90482 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7791a6e4-e5d3-3854-9351-ef6dfba2e640 | -13.20869 | -48.52078 | 2025-10-02 05:57:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9f5b65d4-557b-3fd7-acb5-d69658e852b3 | -15.25985 | -49.30304 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ca499960-c31e-34dc-9fed-825094bc5758 | -17.16543 | -47.03088 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6a09afb-935c-334c-ae9f-5d06fb7a68ac | -14.65428 | -48.25927 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87860ba3-8ab5-3361-b92c-da689cd4f1a4 | -12.80969 | -47.01434 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| efe09a03-1488-371a-9ec3-c822dca4482c | -16.36776 | -47.05522 | 2025-10-02 05:57:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 96a551e2-dddc-3ab0-bbb6-0ddf4756aa86 | -16.04705 | -50.85577 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 30e95243-6176-3752-b000-e8b216a77598 | -13.75311 | -47.98944 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 530d6151-589e-382e-981f-e80f1612a597 | -13.21156 | -48.50224 | 2025-10-02 05:57:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 73365d33-bf0e-3ea0-9498-f0441a1f31e8 | -11.59781 | -47.22058 | 2025-10-02 05:57:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9eb60eab-3b9c-39e1-9687-27fdd5f1eef6 | -14.02131 | -47.98604 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 79178561-9d39-3b58-875c-cb87cb08a8f5 | -14.31761 | -45.98822 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 59c2a440-d4f6-3979-87fb-784d2cf8837f | -14.98681 | -46.9121 | 2025-10-02 05:57:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| efaf8983-4059-32c9-8854-8fe63533908f | -12.70082 | -48.58146 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 52bb9f18-afd8-3d17-83af-d6e8cf035bac | -13.55474 | -47.28602 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 030a8821-e773-302c-a9e5-e054dba2ac9a | -13.24462 | -47.32935 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a984205-ab95-3fc3-b211-6c6641ae80ff | -11.5893 | -47.63226 | 2025-10-02 05:57:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9068c848-60d9-3557-94f9-6f362a201888 | -11.58793 | -47.64126 | 2025-10-02 05:57:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 36b27a21-2b86-36ea-8d1d-6c73944bc95a | -12.9421 | -46.37554 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 73d9d3ae-0d0a-3135-8762-d6ba31e67aa8 | -12.25452 | -47.82227 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6cd81e6f-0c8b-3d32-8772-4a0857cfb3c5 | -13.36692 | -46.6287 | 2025-10-02 05:57:00 | AQUA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f748dbbb-878e-3132-a889-97c734002041 | -13.29865 | -47.20923 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fac4b0ea-60e7-33de-b4cc-1e7fb8993481 | -16.04525 | -50.86674 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 34206fce-4854-32b9-a704-5df0abae2fdb | -16.03737 | -50.85419 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6016256f-0ffd-3d43-9a0c-ba35356af3cf | -16.04854 | -51.02963 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e6dbcae-d403-3976-b421-62448214e9c2 | -11.62188 | -45.0537 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b1a69cc1-5c08-3edd-bda1-8d7ef9baafe4 | -11.61559 | -45.03236 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ededfbe2-3a97-3f60-b013-b15892d697d0 | -15.18894 | -46.40472 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b7a93a92-2e0f-36d1-bf55-718a223c8d15 | -13.3045 | -46.98939 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c3a3a879-4cd8-397b-b30b-cd7d9dc5e4be | -17.09437 | -48.55739 | 2025-10-02 05:57:00 | AQUA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9308fbf-5948-3527-87c4-122e04ca6b5c | -13.15945 | -47.83121 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 22964476-b556-38c3-8d89-555cc30213db | -15.94641 | -43.33745 | 2025-10-02 05:57:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ad29e23f-9561-3ee4-beb0-7cb649cdde6f | -13.32502 | -47.21328 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f2e19d07-9397-381a-b56e-7a0c81b3fe52 | -15.69922 | -46.25279 | 2025-10-02 05:57:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86f3638c-b93d-3bac-ba8f-6cd0905aa3c6 | -12.68724 | -48.55041 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1c444abd-0815-33ac-85b6-3ffd4ede87dd | -14.20806 | -46.11193 | 2025-10-02 05:57:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| dd822bf0-c657-3fc4-a4ba-38f4c32ac39f | -17.17439 | -47.03223 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a58314b7-adbc-35c0-b1df-8cef722edf2c | -12.88679 | -46.93193 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6bbc32bc-14ce-331b-9f77-ad78fc46a7e3 | -13.9578 | -48.10581 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7fa149e8-2e90-3268-952e-02a9d25138ea | -17.18335 | -47.03357 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 957a7a5b-ac5d-3934-83b3-dfa4871ae463 | -11.87493 | -45.01838 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a39f072b-e2f6-34f7-9218-a067cd4eafaa | -12.21729 | -43.7547 | 2025-10-02 05:57:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 919c8dd7-e092-36db-bd56-8000f8a09782 | -13.7951 | -47.53441 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b633e6d7-d906-368f-acb5-3b725f788d96 | -14.98816 | -46.90288 | 2025-10-02 05:57:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64cb9040-2e4f-3bb0-9245-b3902c070566 | -19.51881 | -43.60977 | 2025-10-02 05:57:00 | AQUA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 35045e9d-889d-3825-8aec-bbde75deaf84 | -13.00998 | -45.20193 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 24d2ac05-eaf3-3cd0-8253-dc93eb8cb7f7 | -14.41535 | -46.1454 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6343cc8f-4b70-3dda-a68c-3885e0a27629 | -14.5989 | -48.32542 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c983ca6-964a-3270-8da3-a7e17e87b364 | -13.69368 | -48.6165 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 89592d72-5ddb-3bec-af1e-c5292771f00a | -12.89962 | -46.90635 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b037a0d4-23e5-3336-9dcd-84b86fdfbb82 | -13.22158 | -48.43738 | 2025-10-02 05:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a1106ff8-a182-3fa1-b622-8225ad915a78 | -13.53375 | -47.24598 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 85429cff-cc77-3dd0-9619-57b5340ed922 | -13.70262 | -48.61795 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8578ced4-86e8-32fe-8622-904b8bb6c817 | -13.39739 | -47.77912 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ad7c7636-c03d-39cf-8b2f-6a35a27feb4b | -15.2508 | -49.3016 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 95093d17-0251-3d53-a7ba-ff884a829748 | -14.86249 | -48.29273 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 17bd1990-f964-3d16-8ccb-52805f4dab97 | -17.16679 | -47.02142 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60d283dd-e0c0-3794-8bef-9548de834058 | -13.5663 | -47.58755 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0deb9e81-bf8a-3067-9fb1-72858cb1ae9c | -14.69138 | -49.62393 | 2025-10-02 05:57:00 | AQUA_M-M | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 863d1990-ad0b-335c-b260-851ebe348903 | -22.28136 | -46.70959 | 2025-10-02 05:59:00 | AQUA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| bdefd61f-d088-34e8-ba59-1344014c1df0 | -22.85979 | -50.0786 | 2025-10-02 05:59:00 | AQUA_M-M | IBIRAREMA | SÃO PAULO | Brasil | 3519501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 3cb411f7-562b-3afb-ad58-bd0e5a2c5c5a | -22.85832 | -50.08817 | 2025-10-02 05:59:00 | AQUA_M-M | IBIRAREMA | SÃO PAULO | Brasil | 3519501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| c486ab28-542c-3242-bef9-4163f0ae5534 | -19.72599 | -45.88645 | 2025-10-02 05:59:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85e72258-dd4d-3e23-b4a5-0ad04fe66aad | -20.84344 | -49.42153 | 2025-10-02 05:59:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| aad29784-202b-3ded-b8bf-aa7431e10375 | -22.56755 | -46.78112 | 2025-10-02 05:59:00 | AQUA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 3f80fe50-eea3-3a60-a9ca-ae51187001b7 | -22.02304 | -47.40287 | 2025-10-02 05:59:00 | AQUA_M-M | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 9cc48848-c309-363b-a6f7-680f0f21792a | -22.0216 | -47.41328 | 2025-10-02 05:59:00 | AQUA_M-M | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d9bcfd68-4131-351c-9c22-0b649cd3ec34 | -22.27849 | -46.73139 | 2025-10-02 05:59:00 | AQUA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5baf152f-3930-3e55-956a-ba773dfe777e | -22.27704 | -46.74237 | 2025-10-02 05:59:00 | AQUA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 33d2269a-01f1-3c43-a917-85272912c4c3 | -22.27992 | -46.72051 | 2025-10-02 05:59:00 | AQUA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 17bd82b0-862c-36f3-b9c9-aed3f0b54b76 | 2.45916 | -60.91573 | 2025-10-02 06:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00567a0d-1f1e-36d5-a39f-cafb931ccdf3 | 4.25839 | -60.03509 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed5a3c01-b46c-3d5a-9b99-13f5e2eca37f | 4.25291 | -60.03548 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe9ed87-f1c3-34de-8e5a-d88404498af0 | 4.25617 | -60.0221 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a4e345a-ebdf-38a3-b33a-85239460015e | 4.25786 | -60.032 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 677d1454-53ff-3ba9-8555-c5a5a92c7b5c | 4.2506 | -60.02195 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b603064-aec6-321e-b9a1-06cdc5e67b2c | 4.26293 | -60.02927 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 492a7ef6-5bba-32ae-ad5b-edf3a987bb89 | 4.25674 | -60.02545 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb8e847-81bc-307d-bebf-3ae10e35ee04 | 4.26341 | -60.03207 | 2025-10-02 06:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb5c4cdc-0166-3bb2-be1f-92e9128218fa | -9.4115 | -63.68856 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95db358a-9cb8-3f91-8e84-f81809683f7a | -7.87277 | -71.71579 | 2025-10-02 06:12:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a00c8b5a-e35f-36b4-afaa-c44f1c2a2396 | -9.49119 | -63.13085 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b5231ea-f41f-32d7-aa14-676cf227fcc3 | -9.4007 | -63.6903 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc7a5f5-1d7c-35e1-a4cb-682e6803daa8 | -9.40545 | -63.69427 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4069d393-f622-3877-8511-55ad3645d428 | -9.63986 | -63.20056 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc49f389-5591-3610-9849-b6c829cdd8d3 | -9.49657 | -63.1317 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d261bc3c-1332-3d94-a9d8-0b1a5625b5e8 | -9.40028 | -63.69347 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03d19af-22c7-3732-be3a-0e4cf124865d | -9.40588 | -63.69107 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e226ba0-56f3-39c9-9271-9c11dd048fa0 | -9.63788 | -63.20125 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936090c7-98d3-3d7f-abdb-a033f7557b99 | -9.63448 | -63.19981 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7d98641-e71d-33e5-a1c7-430cbb738de7 | -9.43405 | -63.71713 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9a2100-8212-3a1c-b8f3-2aa1b5a7e414 | -9.42886 | -63.71647 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d2b887e-b556-368a-9b37-94587328c89b | -9.40631 | -63.68787 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README142.md)
