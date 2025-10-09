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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb455a7-80ef-3101-880c-001d5ca760ae | -16.40627 | -43.50351 | 2025-10-09 12:19:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f3a39566-1fa7-309c-888d-b67fcb391c3c | -13.82967 | -45.83717 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f00cb9b7-b313-3808-b58a-3f7df6faad12 | -17.63589 | -47.23072 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 68992d31-6d96-3f21-b6b9-cab7b45a0ec7 | -14.88275 | -48.24925 | 2025-10-09 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6901c5c0-3e8f-3e9b-af43-d2f7d0483160 | -15.77976 | -50.27316 | 2025-10-09 12:19:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 530068b1-4ed4-3381-a507-f26d7323be44 | -13.8018 | -45.82207 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1017473f-abb7-36f6-8348-e615a296a716 | -11.98194 | -45.21859 | 2025-10-09 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 665ad072-b75a-350c-8c37-b2cf4859a74e | -13.37769 | -47.21685 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 19a78f0f-9980-3ea5-a81a-ea0c73ed2208 | -17.24972 | -48.11245 | 2025-10-09 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9936880e-3ce2-3fab-8e9d-ed56853a565e | -15.23079 | -46.36153 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 7a3a169f-dd63-36fa-a502-5a81ab59fecf | -11.52467 | -42.8691 | 2025-10-09 12:19:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9659abff-c17f-3f4f-830e-c25cfb8f28bc | -12.68725 | -47.67488 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 8d3959ab-d7ee-3ec3-8036-33510ade0ff8 | -17.95551 | -45.00659 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 10df2d3a-c436-36b5-8508-84a85c7927aa | -13.79891 | -45.84449 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 659f47a2-4ac2-38aa-9b19-4f63b8abaf21 | -13.83258 | -45.81496 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6b20d345-136d-3f02-9c88-23991244176c | -14.97341 | -46.29662 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 2f59d742-06fd-3ffc-b8ee-c311e8d4c575 | -12.4285 | -45.71289 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| dafce628-fd17-3a13-921a-c7172817cd3f | -11.65832 | -47.52566 | 2025-10-09 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 6377c460-eb45-3e14-9347-1132d58a0e74 | -13.83797 | -45.84967 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 32acb790-a0a7-3571-a579-c2101bbfe3b8 | -11.76764 | -46.41091 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| ea3df3d3-fff1-3729-9232-6a0bce755dff | -14.51641 | -47.29989 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1d056a81-2f7c-386e-bd93-5f41fdff885b | -13.07606 | -47.79863 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 25c88681-9492-3de2-808e-b5717f56b2b5 | -12.64106 | -45.01421 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 9e96e45d-9cd3-3c05-9659-1085b4c38c1b | -13.36064 | -47.99855 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ea6ba080-15aa-3511-919e-e6fa23023b0b | -14.40635 | -46.02029 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 93632b5d-aa3a-3759-b275-6bb00fe2e0ae | -13.36864 | -47.21543 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 20c0b009-af2b-3f60-9e41-f97426adc41d | -15.74921 | -49.03352 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2ac62fb7-4b8c-33e9-bef2-f19b5a25fa9c | -15.49317 | -47.96554 | 2025-10-09 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 815a7298-dd8c-3c5e-a28b-2b64f3ad2a19 | -15.23189 | -48.19218 | 2025-10-09 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fe609afb-53c3-3dc7-a141-99a80eccb43a | -11.48308 | -43.48361 | 2025-10-09 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b530f0c9-2f84-3850-81b5-4e932991901d | -14.4422 | -47.97543 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 24860f45-3083-300d-b487-4aac8663649d | -10.43451 | -46.5917 | 2025-10-09 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2c06e0e9-f81f-36f6-b588-4d8937cd9e5e | -14.84935 | -48.42229 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 777b5fc6-ddbf-3ae1-a90f-f5ab7b9aba97 | -16.28382 | -47.14674 | 2025-10-09 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 94efa53c-ca24-3d8f-b148-7f1ca6647a9a | -18.05183 | -44.96507 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7b4a9285-becf-3e9b-a1f8-f0876fc2b148 | -17.64535 | -47.23196 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 97e5db6c-99c4-382e-ace9-9cf2e50d3bf5 | -12.95206 | -42.49571 | 2025-10-09 12:19:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 2ba1e750-fde0-34e6-9c4c-a5323e61ec9c | -10.22871 | -46.08478 | 2025-10-09 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cf03c800-d41c-3e7f-94a8-50a22b310aba | -12.42596 | -45.70667 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b93c005b-8459-39b7-8e44-31c44b741734 | -12.46848 | -45.48183 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| efea783d-4b2a-393c-b1d7-8da5c7ec6384 | -13.35938 | -48.00749 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a0d13937-41c4-3fb8-a57d-5e444dddfe04 | -15.75051 | -49.0244 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de42cf4a-cccf-3fd4-881c-8850ab05e0ad | -17.94455 | -45.00488 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1efa3d93-4126-35b5-abd0-c765f76a6930 | -14.40979 | -46.01538 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d341cb3a-b587-33c8-a359-8fecc90ef2b1 | -14.5244 | -48.69995 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d2742045-3924-3568-b7d8-f04ab66fc244 | -17.6547 | -44.45116 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 841d8efc-8751-3e1d-b34e-8d2a7b68c705 | -10.18035 | -44.5641 | 2025-10-09 12:19:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5a5f402b-1218-38d3-a046-ab5fd162c8ce | -13.2487 | -47.6135 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 64cf3634-2c52-3b28-baf7-5341e0d35555 | -12.42448 | -45.71757 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d6fb8c21-e30d-3c01-82b5-0560fc61290e | -13.38681 | -47.21778 | 2025-10-09 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cb025307-ffc8-3c52-b39a-a328e1e9f8f8 | -13.23846 | -47.62142 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ace3890f-4cb9-3e07-83cf-72bd69212556 | -13.05418 | -48.0189 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 91cefb17-27dc-3ab4-b4ae-e36d8236a186 | -13.08626 | -47.79068 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f974ca5b-41ec-3ce5-a346-6edf041200de | -18.86703 | -44.11297 | 2025-10-09 12:19:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 01abc3c2-bd49-301e-b59b-28a978cd8904 | -15.23219 | -46.35086 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f0dc56b4-85ff-3125-922d-c84b6af69df3 | -15.76326 | -48.99835 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ad1e6cd-c023-3b26-8808-4c2233a285d5 | -12.42299 | -45.72848 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 96f4d419-ae30-33af-9593-64320bf1f7a8 | -11.7787 | -45.05571 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9fb8b5af-aa5f-39db-ae56-84b9b83d2beb | -12.63951 | -45.02621 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 5a92f0ae-cee9-388f-812a-0735b5e3e6f8 | -17.64677 | -47.22133 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0b4cd337-6192-3888-a61b-85d12c0d6e83 | -12.68854 | -47.66571 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d8bc6beb-3eab-36d7-ac8d-515d1d2f8166 | -13.44293 | -47.60738 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e67b9f0c-084b-3762-9bc6-db4d7e9ddaf9 | -13.34998 | -47.54865 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b6c6bfbf-b547-3f3c-83f6-c1e5acee7dbd | -16.59403 | -46.54824 | 2025-10-09 12:19:00 | TERRA_M-T | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95aa502f-a733-3cc5-8da8-5f24b5e2f5a3 | -13.05547 | -48.00982 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e6a0e52c-860a-3db5-8044-2002f7700580 | -16.45253 | -47.61417 | 2025-10-09 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0360b1cd-6198-3396-8464-3ba49b814f88 | -14.71854 | -47.44032 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 42f89775-00ad-382f-b77e-8332b1ce0fa3 | -11.0881 | -47.18736 | 2025-10-09 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4beca4ab-4b7c-37cf-bbde-88b8792132c2 | -11.98345 | -45.20713 | 2025-10-09 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| a6ef071c-8f3f-3dad-af24-60d93d5c904b | -13.42764 | -47.58609 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 4ea54a5b-6321-3264-8cf1-5a6d6cab2dbf | -13.04653 | -46.81063 | 2025-10-09 12:19:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bbab6414-c60f-3f48-836a-407892e2da06 | -11.77629 | -45.15455 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| db830efa-7f33-350b-939a-70ad7057ef30 | -13.43267 | -47.61543 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c2282299-5114-3289-ad15-00fcb5c9e32e | -13.36605 | -47.76598 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4052793a-36a9-33fe-bea0-26d329c2e79f | -17.47514 | -45.46804 | 2025-10-09 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e8051a21-a9e1-3705-bbaf-7227e8d2cd69 | -15.98203 | -50.832 | 2025-10-09 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c02451df-d528-3ee7-9b3c-91bd959eb336 | -13.80868 | -45.84573 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 80ad30fd-161c-3ad2-8c95-1e6b7abc0ff5 | -13.11116 | -42.99962 | 2025-10-09 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 66775e14-3fc0-31db-974e-2b6485cd681d | -13.82572 | -45.79122 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 024a5b10-3c4b-3a03-8c29-ee38b15ee042 | -11.78624 | -45.1558 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fa00899f-5d80-3f53-81d2-9e5e83f37609 | -12.27401 | -43.11254 | 2025-10-09 12:19:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 38a02107-ae59-3dd7-9e84-1331b59b8dea | -17.65653 | -44.43527 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 41.3 |
| fa2269f1-b30b-3868-a75e-0ae100d09b0e | -18.22704 | -44.33971 | 2025-10-09 12:19:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 39152549-1232-33ef-9b48-3e661f2d6aab | -15.23187 | -47.32439 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d242eda-3079-3c1f-8083-a660057b4311 | -13.36953 | -47.99974 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d3071598-8803-3611-92e6-8ed45a2c93e8 | -17.37269 | -45.07916 | 2025-10-09 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8b228d7c-703e-3ab0-a5df-4b2638c05580 | -17.94623 | -44.9905 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| ffcb1916-2927-3ae9-86b9-f4cb07ce6c3d | -14.82159 | -47.22144 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 20125092-6628-3647-bbd6-3dfbade6b44f | -13.79312 | -45.88926 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 37c59fcc-123f-311d-8f45-f4431ca22b79 | -17.58614 | -47.16973 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b923ff28-c7de-3bd6-a726-2e14d64e996f | -15.29727 | -46.15646 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ed52bb40-5f9c-3c96-9a9b-f95fa51409dd | -12.2526 | -47.88541 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3579a723-9bf0-31bf-a605-5ed44ba98031 | -13.32601 | -43.57594 | 2025-10-09 12:19:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a787bd05-a9b6-3736-bb20-f2f0c4574c87 | -14.98947 | -49.94125 | 2025-10-09 12:19:00 | TERRA_M-T | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0634880a-86d5-3996-ac1a-6444c8a29221 | -17.00208 | -47.76969 | 2025-10-09 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0a9aea6a-a952-33ca-86e6-b2541e3c2c80 | -11.77774 | -45.14339 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f07036c3-3e6b-3785-8fd7-7547e4a94aa8 | -11.65703 | -47.53481 | 2025-10-09 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f04df5ae-e3e8-381c-8164-e9a4c371b7e6 | -14.41958 | -43.98103 | 2025-10-09 12:19:00 | TERRA_M-T | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| df318d7d-2d5d-3eea-b1e1-4e5173167112 | -13.09388 | -47.8012 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 78e3c156-057a-3906-a72d-5cc6cfdd4085 | -11.78032 | -45.04374 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |


[Clique aqui para ver as próximas entradas](README65.md)
