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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49968238-ed43-3b5e-af54-3993c7e5fbde | -8.0604 | -48.664 | 2025-09-10 01:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5af15e0d-9444-3820-89ba-c455dd898945 | -11.4465 | -43.6224 | 2025-09-10 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 848a3895-cf05-3f0d-8d4e-643233dc39f5 | -13.1176 | -54.9191 | 2025-09-10 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d4b2c7c1-a7c9-3600-9c7a-c8d7e0a879c5 | -5.5705 | -45.0291 | 2025-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 2cdda364-1a27-3bdf-bd4e-ca3946b24750 | -13.1367 | -54.9171 | 2025-09-10 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cfa74455-2c05-3826-a6e8-b989b8193ea6 | -11.1184 | -48.4589 | 2025-09-10 01:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1806fd7f-eaea-3bea-8e07-8b863ca8973a | -21.0079 | -47.9984 | 2025-09-10 01:30:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 59f1e6c6-fe45-389f-be99-143520efd86f | -8.0602 | -48.6856 | 2025-09-10 01:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 128.2 |
| f26d2553-3264-3281-b2db-976f9afc72bc | -5.5892 | -45.0278 | 2025-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 274.2 |
| c11b3d82-e975-3caf-8314-b3a6229c0aac | -18.1325 | -51.7096 | 2025-09-10 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| cf6c13a7-9bd5-36b5-a326-cf2d65404e2a | -18.132 | -51.7315 | 2025-09-10 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4433e4ea-3f26-36f8-9328-3b0a945ec01a | -20.988 | -47.9798 | 2025-09-10 01:30:00 | GOES-19 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 134541c7-2a5a-352b-88a1-5417cf8cdadc | -20.988 | -47.9798 | 2025-09-10 01:40:00 | GOES-19 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 150.1 |
| a1d934ed-d9d6-3208-93ac-63b3fa5c5541 | -11.3393 | -46.5193 | 2025-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e5ee186a-17b8-378c-8a7c-91fa3b10b79b | -17.6141 | -40.219 | 2025-09-10 01:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 157.3 |
| 9ac7afd1-e6a1-34de-8d9a-e0f704c6cb03 | -11.4657 | -43.6195 | 2025-09-10 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 2cea42b8-8f61-30c7-b383-01add86f1a4a | -6.2595 | -43.4129 | 2025-09-10 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7783ae9a-14fd-3bc1-94f0-0e7c831d6bbe | -20.9873 | -48.0033 | 2025-09-10 01:40:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 172.0 |
| c7946ea5-e334-3ff0-a8b2-f6d73227b9ce | -5.5705 | -45.0291 | 2025-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 8b714b52-b257-303a-bac4-a657eb4b2b55 | -16.0604 | -49.9741 | 2025-09-10 01:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b1a74ebf-0705-3b9d-a74f-cd96cfbde5a5 | -6.8521 | -47.9143 | 2025-09-10 01:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1ede0003-7c64-3b0b-841c-cd86e5b7b818 | -13.9762 | -48.224 | 2025-09-10 01:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 28340dc7-f26b-3a7f-8e79-d4e439d7bcd2 | -6.8519 | -47.9361 | 2025-09-10 01:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ebe35784-792c-3522-b55b-4aeb8245e47b | -12.0117 | -51.0104 | 2025-09-10 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cece7bc8-290f-336b-8e36-ef9a5ea9d7bb | -17.6133 | -40.245 | 2025-09-10 01:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 11e6b742-5f2a-38e8-95cb-5549f9bdc72a | -11.3389 | -46.5419 | 2025-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 589b8bb0-0ddc-32e9-a838-e53ac51fe086 | -15.8869 | -51.8274 | 2025-09-10 01:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 58d8a0ba-75bd-34d6-a352-b7aaf728211c | -21.0086 | -47.9749 | 2025-09-10 01:40:00 | GOES-19 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b3c4c290-ea9b-3110-ad26-aa8733484503 | -21.0079 | -47.9984 | 2025-09-10 01:40:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2ca2a227-87b1-3537-9884-70ff4f580b16 | -12.012 | -50.9891 | 2025-09-10 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9b44e052-ea1f-35cd-8ed4-632adf36d5a8 | -6.2597 | -43.3895 | 2025-09-10 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4bdeba24-c8fe-330b-8322-19750cf8a941 | -18.132 | -51.7315 | 2025-09-10 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1046ff9c-2755-3766-9fb9-17d61faa4ddd | -5.5892 | -45.0278 | 2025-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 86288b94-4f25-3e7c-95d7-5e45ef5ae32a | -23.0349 | -50.0908 | 2025-09-10 01:40:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 6c9299d7-e9aa-3bbb-be7e-fd0cddea1bf3 | -11.4465 | -43.6224 | 2025-09-10 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 6b82f86b-4410-354d-9e4a-55a4d63c013a | -5.5703 | -45.0518 | 2025-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 59de48c3-f18b-37f1-bf6c-722184728a3e | -23.0342 | -50.114 | 2025-09-10 01:40:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| 8640bca9-1f27-3bdb-b63e-0ebc1aaffcc4 | -11.4652 | -43.6432 | 2025-09-10 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 86efe303-acc9-3174-b991-c4a98b3829b7 | -5.589 | -45.0505 | 2025-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 1b7a981c-be87-3f47-9d54-b9ea50011887 | -8.0414 | -48.6873 | 2025-09-10 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 97cd7d8d-31ba-3d18-8750-f4cc656b0753 | -8.0602 | -48.6856 | 2025-09-10 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.2 |
| dabda622-2332-3ae0-89fa-79a0d9aedee7 | -11.488 | -50.4298 | 2025-09-10 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3c5bc9bd-6513-3092-be11-69e487d07221 | -15.8397 | -52.2631 | 2025-09-10 01:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d409fdd5-6079-3b1e-a0a7-3f2ceff9d0e6 | -16.0408 | -49.9773 | 2025-09-10 01:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 668b6fcc-ae85-359e-94a1-cf96cf606191 | -11.4883 | -50.4083 | 2025-09-10 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 30eb06c3-1c89-3245-9877-d290f5d7b34d | -11.4469 | -43.5988 | 2025-09-10 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fe8082d9-b1ff-31d7-bd33-31ad7a1481aa | -21.0079 | -47.9984 | 2025-09-10 01:50:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e7e8f6dc-1bb5-3718-a54a-cb3823d664e2 | -21.0086 | -47.9749 | 2025-09-10 01:50:00 | GOES-19 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1472d663-2a0d-3a32-90b2-6d054bf4a909 | -5.589 | -45.0505 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 6e8e2af5-0fb7-3755-ab2f-0584cca1ffcd | -19.6476 | -45.0374 | 2025-09-10 01:50:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2b441d0d-ed71-375c-8d87-19cae5c04e4c | -5.5705 | -45.0291 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 1f38f2f7-7ad2-387c-a8b1-6a35d063de3c | -6.2407 | -43.4144 | 2025-09-10 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 00fb1cf5-b5fc-3de5-b6e4-6e65fbbe48e8 | -5.5703 | -45.0518 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 37f4d9ea-e396-360e-a432-261e2dd26156 | -8.0602 | -48.6856 | 2025-09-10 01:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.3 |
| dedbede4-9dbc-3bde-a6c2-6c8eb56ae11b | -5.5892 | -45.0278 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 097f6368-1bd7-3ef7-90d7-0d3e782e975d | -17.6141 | -40.219 | 2025-09-10 01:50:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| e3086c4d-5ba1-327c-af0a-2c8c064096e9 | -12.012 | -50.9891 | 2025-09-10 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4a3b14a1-e785-319c-a1e6-728dd4762e17 | -8.0414 | -48.6873 | 2025-09-10 01:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 47df5d8b-e44a-3aec-aa45-14d686cb8f14 | -11.4465 | -43.6224 | 2025-09-10 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5089cc0d-9035-31f4-92a4-dd4fd93d3d93 | -20.9873 | -48.0033 | 2025-09-10 01:50:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 6a97ff8c-d192-3ecd-9197-cce38c828254 | -11.488 | -50.4298 | 2025-09-10 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9198212b-9a9e-318e-80bd-0a551b6f6e67 | -20.988 | -47.9798 | 2025-09-10 01:50:00 | GOES-19 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 64afdc3f-4aef-37a3-9d85-990e6ad179ce | -15.8592 | -52.2602 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e85a6a3f-a369-3d1d-aa5e-61ae4327978b | -20.0198 | -47.6225 | 2025-09-10 01:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4ece81cf-e6fe-38c4-9592-11e593305e24 | -6.2595 | -43.4129 | 2025-09-10 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 47160281-6845-3e36-8bd2-cf401e95c47d | -15.8397 | -52.2631 | 2025-09-10 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 56b4f8ee-c06a-3f0f-ac23-3fe9d27a4d34 | -11.4657 | -43.6195 | 2025-09-10 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 36c0542d-01da-349b-9907-dc0b87197af5 | -12.0117 | -51.0104 | 2025-09-10 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3767d481-7106-3a65-af0a-09818e96738f | -5.5705 | -45.0291 | 2025-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 8e914a37-9297-3e76-b2d7-3e8e437d095d | -8.0414 | -48.6873 | 2025-09-10 02:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 116542ae-a1d1-344d-bac8-bc4fb63795f2 | -13.9762 | -48.224 | 2025-09-10 02:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 54c70088-607d-33bb-9c02-c4a23b3f2875 | -11.4883 | -50.4083 | 2025-09-10 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 0632d097-435e-3855-bfba-824bc1f88733 | -13.937 | -48.2522 | 2025-09-10 02:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 37083159-439a-3607-a08b-b4cd92ea18d6 | -19.6476 | -45.0374 | 2025-09-10 02:00:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f7a87fb5-a9e8-3271-b5bf-a2b5f031332b | -8.0602 | -48.6856 | 2025-09-10 02:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 912123e5-8079-345a-9b6c-c0108b6ea875 | -6.2595 | -43.4129 | 2025-09-10 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 5e2ea721-ed48-327a-ac27-8b8b896e95e9 | -15.8397 | -52.2631 | 2025-09-10 02:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fc92543d-2dfc-3e18-8e2d-2d83008332bf | -12.0117 | -51.0104 | 2025-09-10 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| e8a94a2a-dc32-30c4-ac63-16be7851509d | -5.5703 | -45.0518 | 2025-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 37d6af91-ad12-3fb5-82d2-ae69d38e103c | -12.012 | -50.9891 | 2025-09-10 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 797b0fc5-196e-380b-9ae0-b9d2dc0f0ebe | -11.1184 | -48.4589 | 2025-09-10 02:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8eed7b9b-7bc5-325c-8044-0e52b60985f3 | -11.488 | -50.4298 | 2025-09-10 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 5cf31991-d144-35e5-b3e5-6f7a1e0d1aa1 | -11.4657 | -43.6195 | 2025-09-10 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4e782c52-96bc-38be-8a00-1dba65a31a56 | -11.4652 | -43.6432 | 2025-09-10 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e12c3917-c5ee-3b7e-9608-b351f7808f22 | -5.5892 | -45.0278 | 2025-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| e92a45df-d96b-39b8-b0da-7bcdb4bc35bd | -11.4465 | -43.6224 | 2025-09-10 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1498f470-5946-3b1d-a219-96d7602e25a0 | -11.9929 | -50.9913 | 2025-09-10 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1d94d20c-f50c-3db0-b6c8-bdc4d8787067 | -5.589 | -45.0505 | 2025-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 7064667d-5b4b-3841-ad9c-a00b58b1cd79 | -11.0774 | -65.19103 | 2025-09-10 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4a4bf43c-f44d-37be-8e2a-350e634b4942 | -12.0117 | -51.0104 | 2025-09-10 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 339d812a-ff1f-3d23-8850-8c1cbdc42988 | -12.0492 | -51.0487 | 2025-09-10 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 075857d2-073f-3434-a39f-c72357ed791e | -11.507 | -50.4276 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 706e9d6d-220d-31ff-9c90-5f3aaf471967 | -12.0304 | -51.0296 | 2025-09-10 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| d1219a93-2620-302e-98d1-1f2eff8a5bf5 | -20.0198 | -47.6225 | 2025-09-10 02:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1dcc131c-889e-3cff-90d6-4f95b5fb06b7 | -11.5073 | -50.4062 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b8d9dfa7-2ee4-38bf-b56e-bf306e74cdd3 | -11.488 | -50.4298 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 0786497d-4758-32ac-88d9-b6edf9e18b5b | -11.9929 | -50.9913 | 2025-09-10 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 54ee4e1e-30ec-3a88-ab9f-4a5e60af1b4b | -5.5703 | -45.0518 | 2025-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f9772498-3e5c-358f-aed6-2e4d6b3b70ce | -11.4693 | -50.4105 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| bd6e5be9-8012-3202-b3f5-348f26ef7d37 | -6.2595 | -43.4129 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README13.md)
