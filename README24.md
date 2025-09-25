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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c46272e-0bc2-3a68-8225-0a34ffcae124 | -17.03015 | -52.24006 | 2025-09-25 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fd744d1-04ff-3c24-a3a9-a726ee1d18bf | -18.79268 | -50.92416 | 2025-09-25 04:36:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0590dfe-9891-325a-8bdb-edb0d976ec80 | -17.94142 | -55.86215 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 71c083a0-fe07-320e-a9cc-9565bdd79c20 | -16.85793 | -50.506 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06361963-0816-3785-a47a-3022bd1872fc | -17.93675 | -55.86499 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 629375ab-7418-3ab6-8863-566f08247138 | -20.98049 | -50.01682 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 7df9d69a-bd18-3d7b-ab27-bed8e7d81a93 | -15.76805 | -59.50124 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a7b1d466-23b6-311d-b54d-0e66a09db440 | -17.92944 | -55.85975 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 54a7913e-93c9-3c15-ba19-05c80eb291d9 | -21.01348 | -50.02633 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 40b24621-ece1-358e-a51c-28b46744bb14 | -20.98851 | -50.46199 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9d20264-dd29-36ba-891f-574feb5671a1 | -15.90795 | -59.34925 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60ce89fe-aa8e-3302-b76c-b473d5b49656 | -20.99391 | -50.01912 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d518e508-c02f-3f72-a26b-0d8941cad9df | -17.9408 | -48.65223 | 2025-09-25 04:36:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e2764a6-d977-390f-b74f-3566ba6db369 | -15.75446 | -59.48718 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b3bc635-dc5e-384c-9fde-d7faa7cf3a00 | -19.1741 | -48.78821 | 2025-09-25 04:36:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1605dbca-9648-3317-ae5b-e460bf7e80f9 | -15.76865 | -59.49644 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1e4500af-8814-3b68-beaf-2781d40aad1a | -15.92319 | -59.3494 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3a68f2-5f4c-3108-a4ce-6c5cbfd6defa | -15.97381 | -59.50597 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5309bc6b-a8ae-381f-93c1-84ff1935e967 | -18.87833 | -51.52151 | 2025-09-25 04:36:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7ad0ca5-d9f7-3ddb-b709-437f1c0b10bb | -20.99681 | -50.47489 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f2820ca2-15cd-3a91-8250-32d282ec6700 | -20.98384 | -50.0174 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| ed1c6e8c-a0ff-3ce2-9bdd-743ab7ac6a70 | -21.00287 | -50.00513 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3e601b48-98c0-3d96-9688-fc7dcf36fc6a | -20.99279 | -50.0267 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 66f8aa3c-df4e-39c7-b199-278a9abd632c | -20.98832 | -50.01041 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 83ed5f56-d428-3c8a-8346-82a45d18f226 | -20.99727 | -50.01968 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 774763a9-ee21-386e-96b5-c29f560e7ace | -17.95608 | -55.84997 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 971cd6d7-39a6-35ca-aa33-64281840500f | -21.00564 | -50.03275 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e9245155-ec8a-3c73-8882-d67d129a9957 | -16.85238 | -50.51978 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9c096837-2f4e-3d29-8b74-a36064ef2fca | -15.77009 | -59.49095 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8d3f299b-ca88-30af-ada1-8f05481919fa | -20.98795 | -50.46573 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 094df6fa-6660-3d6d-a540-58fda0a3b870 | -20.97545 | -50.02763 | 2025-09-25 04:36:00 | NOAA-21 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| df5875a9-0756-31fa-b40c-1f243ce523d2 | -15.90216 | -59.34658 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05df57b9-250b-3420-80d8-19d72403a214 | -21.16021 | -49.7207 | 2025-09-25 04:36:00 | NOAA-21 | UBARANA | SÃO PAULO | Brasil | 3555356 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 078c9e51-ee71-3054-8af1-f02ff6d1da2b | -15.88072 | -59.34586 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54167253-dab2-3d81-910b-173770bd44ff | -20.98272 | -50.02498 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| f9f0a7fd-3443-3315-9796-4d6e45e294a9 | -21.34637 | -48.09008 | 2025-09-25 04:36:00 | NOAA-21 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 436e4763-324d-377e-ad00-90cb9eb1439c | -16.84747 | -50.50792 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a50f0e-1ee2-3b4a-b96c-1be80e7df8b4 | -20.99223 | -50.03049 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 706b4edb-5f4d-3b8e-a91b-3cf575379456 | -18.8756 | -51.51729 | 2025-09-25 04:36:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f382f12-ff85-3e6e-828f-10ae5f2ba584 | -15.91799 | -59.34839 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002fa7e9-6e98-36b7-822c-1d643fbf7193 | -20.99224 | -50.00721 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9d210749-63ef-34ec-b319-a2963f4ae7d9 | -15.89638 | -59.34852 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00326d5f-3922-3d29-8e6a-c9a6c04ab8ef | -16.8568 | -50.51316 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b9c392e1-ae71-318e-be6a-19f2eeaf9a20 | -20.98776 | -50.0142 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 2f7fa618-81e1-349a-b0f0-1a5d5c5bdda9 | -17.95209 | -55.84917 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| feb0bd4f-ca15-3ed5-b9bd-1c4570affe00 | -15.36603 | -59.17143 | 2025-09-25 04:36:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70959916-c597-3f83-84b8-36fa97ac1e1c | -20.98739 | -50.46947 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 91ed73e9-f098-34e4-918d-39ef3b3ca844 | -18.26 | -51.12968 | 2025-09-25 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41e250de-bcd9-3f50-9706-edbbfce5b3a1 | -20.99839 | -50.01214 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3b32d151-4361-3603-8a12-b03916f2227d | -17.93275 | -55.8642 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 48590c11-a628-351b-96d1-0bec20c7955e | -20.97881 | -50.02819 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| e2705da4-18be-3051-9f11-cf9674e381e8 | -17.92876 | -55.8634 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| d6ce077f-70aa-36b7-a555-7fb4b93b6e6e | -20.98683 | -50.47319 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4440153c-5266-33d1-9533-be37c730e99d | -18.87502 | -51.52094 | 2025-09-25 04:36:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ca264c8-4e24-372a-a07d-cfcc0c641ca9 | -20.6679 | -48.81779 | 2025-09-25 04:36:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 91e6b065-6246-3067-85f0-7ade3137979e | -20.99111 | -50.01478 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 8a5066ef-56ed-36d9-80c7-d2e5a5dd581f | -15.76115 | -59.481 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c780e819-b309-3886-b563-3c2a9c2c8a72 | -17.93079 | -55.85247 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| efec93e5-d44d-395e-9b7e-9bbc5212f009 | -20.99167 | -50.011 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 0bc37cc0-1d85-3385-8b9e-b9176b8f24ec | -20.99016 | -50.47376 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 919ed4e1-fd3d-3124-afb0-6e189fb5695a | -15.82334 | -59.60467 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b757051-45ef-3937-9599-429bbf336386 | -20.97937 | -50.02439 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| 83d9cec8-4bf0-30af-aaeb-1f92595400a3 | -16.84964 | -50.51563 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4049e4ed-c186-39b7-8d4d-7ddf37bf872f | -16.85133 | -50.50489 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28f1758a-e618-3f2e-8f5a-a871739d429e | -20.99447 | -50.01535 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c6f04919-66af-3354-b9f6-a029921b69b8 | -16.85294 | -50.51619 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 18e64e7c-2f8f-3b68-995c-441769dec4d9 | -17.93478 | -55.85326 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 94effaa0-4c05-35dd-a5aa-37151d6138ab | -18.95755 | -49.57788 | 2025-09-25 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8787cb5-0870-340f-adcb-2213b2b7af8b | -15.24757 | -59.44112 | 2025-09-25 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0676afd5-b75d-3d3f-ad9e-d99092849153 | -21.16359 | -49.72126 | 2025-09-25 04:36:00 | NOAA-21 | UBARANA | SÃO PAULO | Brasil | 3555356 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bfabaa1f-a229-32cb-a690-bfe395db290b | -15.75522 | -59.48336 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab63f06d-51df-3770-a7ca-14db06be59ca | -21.00677 | -50.02517 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 935172d6-fdc6-31bb-9aed-aa3095180e25 | -17.92808 | -55.86705 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| c026769d-1759-3e0b-bd8f-b8da38c91f20 | -17.94344 | -55.85122 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 12750a50-cab4-35f5-9ee4-4e36b4c0c3c9 | -17.95142 | -55.85281 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0fc2502b-985c-384c-9cf1-d4d6f90e4249 | -20.98329 | -50.02119 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 6c0e8ea2-574a-33e2-afef-02591f1157e8 | -15.83526 | -59.60007 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6761cdc4-9528-3ae4-be54-48279063f11b | -21.00231 | -50.00891 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 910245c6-60ee-36fc-821c-ee20cda27974 | -20.99184 | -50.46256 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 269da6e4-4a6c-367f-90af-e2e93a92de83 | -15.90904 | -59.39377 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98cddf6e-1d05-392f-a8a7-8fe5140ec2e6 | -20.99335 | -50.02291 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f6fa879f-bb02-3fe1-99ba-dff5b6f0585f | -15.86895 | -59.35074 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb32f452-e86c-3d26-b6fd-5ff7e6ada669 | -17.9381 | -55.8577 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 347f7c48-c666-38ef-8c55-7a60fc515f8c | -20.99559 | -50.00779 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 262741ff-4fce-3e5a-993a-19c2e09c450b | -15.76794 | -59.49987 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 01ad3dbb-14eb-30b1-8c4b-9a84af3f7a01 | -17.93945 | -55.85041 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| adfcd6f7-092f-3d45-81e3-ba639bb6cd63 | -15.86973 | -59.34682 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6985edb-2888-3c61-bd75-5f91585020d8 | -19.14334 | -48.78451 | 2025-09-25 04:36:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3da7e10-b93a-319d-b855-e2dc89c30f19 | -15.90943 | -59.39473 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b23156e2-31ed-3ce5-8aee-83760d203466 | -15.90667 | -59.35108 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2d1b536-320c-3971-a4b9-61e82cd8e4fa | -15.8912 | -59.34744 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0e873797-e8c4-3a9a-b02b-562198e37766 | -15.76279 | -59.50022 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c5d186f9-09c0-38ce-9dc5-fe8f8be76d79 | -18.18688 | -53.33485 | 2025-09-25 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bffc9494-340f-3e6a-84c8-1b8e75ceaea1 | -20.98887 | -50.02993 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0d801615-30c7-310c-8179-615270ff62ad | -17.93208 | -55.86785 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 3774bfd8-64af-3c9a-8bf7-ea63b987ce79 | -17.93411 | -55.8569 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 7849f314-b0c9-3a38-a1d7-b4227d56602a | -15.76722 | -59.50338 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0dcfb849-3050-3519-acf2-23e763ce0454 | -20.99279 | -50.00343 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 87587176-7c1a-3dd4-85c5-0d436b991167 | -18.87891 | -51.51787 | 2025-09-25 04:36:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0a06c22-e46a-3c4c-9a0c-ce71fb1415fb | -18.95699 | -49.58163 | 2025-09-25 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
