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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93a074fe-4f1b-38fe-9dde-a7c6f7523535 | -20.1038 | -44.482201 | 2024-09-28 00:10:52 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb984415-49ac-331d-8d5b-e10f7622de42 | -19.624901 | -42.834301 | 2024-09-28 00:10:54 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 206f7cc8-7121-3e5d-b8da-f5f9a3a4ece2 | -19.6266 | -42.842499 | 2024-09-28 00:10:54 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33b1e40b-9ee9-3722-a4fd-1850d64fdabf | -19.9189 | -43.8452 | 2024-09-28 00:10:55 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c2fe2e2-07c2-3308-a463-ab3f5b13540a | -19.9207 | -43.854401 | 2024-09-28 00:10:55 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ae96331-f86e-3307-a16d-c900da1709f9 | -19.405701 | -42.313702 | 2024-09-28 00:10:56 | METOP-B | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4dbcfb6c-f1ee-37b6-895c-42060646d48c | -19.4074 | -42.321499 | 2024-09-28 00:10:56 | METOP-B | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50121ab2-84d7-3c33-8290-e4ec1a8cf271 | -19.4219 | -42.4916 | 2024-09-28 00:10:56 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7cafe6c-1eda-3c35-85fe-bb46aa37eb90 | -19.4235 | -42.499599 | 2024-09-28 00:10:56 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0500c069-dc2e-3bcd-bbcf-8bcc170d5b53 | -19.510799 | -42.876999 | 2024-09-28 00:10:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ed73d6d-30ab-3eff-8f20-dec2a7a44c81 | -19.512501 | -42.8853 | 2024-09-28 00:10:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 751528b0-7004-3167-859f-098b060719d4 | -19.202 | -40.6213 | 2024-09-28 00:10:56 | METOP-B | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3a8af96f-368b-3294-a836-ccfb57cccbed | -19.2036 | -40.628502 | 2024-09-28 00:10:56 | METOP-B | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a212f19a-e6e1-3e5b-bc17-2f4af10ab587 | -19.6479 | -42.846401 | 2024-09-28 00:10:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 042f6475-cb52-332c-b050-ed15e32acce3 | -19.4056 | -42.561901 | 2024-09-28 00:10:57 | METOP-B | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 097dbffa-0dd4-390b-8958-7bf6384621c0 | -19.3958 | -42.564098 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3699ce76-fc7e-37b2-8d3a-c1df185c0444 | -19.397499 | -42.572102 | 2024-09-28 00:10:57 | METOP-B | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb100bf4-118d-335a-a1e7-7f16f9756c58 | -19.399099 | -42.580101 | 2024-09-28 00:10:57 | METOP-B | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 810b4ab9-537b-3735-a976-f4dc6370b02e | -19.386 | -42.566299 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd089792-b38d-371f-b81e-2dd2d9fc01e3 | -19.387699 | -42.574299 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b87cc1a4-d0b3-379c-8d30-a56ca550958a | -19.389299 | -42.582298 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebab69ed-9495-3d63-9dd2-3135e67caab7 | -19.391001 | -42.590302 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 785df874-14d4-368d-bd40-35b598457451 | -19.377899 | -42.5765 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7c9e5dd-78cb-3422-8793-be102b92fac2 | -19.379499 | -42.584499 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8432946d-c857-3af9-a3bb-bb033f3c762e | -19.381201 | -42.592499 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a3e6eb0-617b-3d30-bc7b-b2f8ff1024ef | -19.363199 | -42.554798 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9b17e7a-8833-3cc3-ba4e-3183c83aab0a | -19.364799 | -42.562801 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4177e2c4-c909-32e0-8d36-f71ead784b69 | -19.3664 | -42.570702 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 003ca5cc-7cb2-31dc-ad18-29a93d823adf | -19.368099 | -42.578701 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb86497a-ea4f-333a-8863-d2b477c27940 | -19.369699 | -42.5867 | 2024-09-28 00:10:57 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14005a51-4322-3076-ba95-aff092aeb0ab | -19.749599 | -44.2827 | 2024-09-28 00:10:57 | METOP-B | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cbd7dd70-89c8-33ee-a70d-870fa36dc78d | -19.3566 | -42.572899 | 2024-09-28 00:10:58 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40d7144c-f35a-3b99-a219-20452e13ccf0 | -19.358299 | -42.580898 | 2024-09-28 00:10:58 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ab26b0f-291d-3a52-8aa4-ef8b91599a54 | -19.3599 | -42.588902 | 2024-09-28 00:10:58 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79f8a0d6-a391-3c59-96d6-426649113e89 | -19.395901 | -43.269199 | 2024-09-28 00:10:59 | METOP-B | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09a9ab74-3ada-36c7-acab-71a6452438e4 | -19.3976 | -43.277699 | 2024-09-28 00:10:59 | METOP-B | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f53b0067-0bd6-339e-9669-d8050de74d98 | -18.941 | -41.272598 | 2024-09-28 00:11:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0cee0e3-9672-34d6-b7d6-f07f3062919e | -18.9426 | -41.2799 | 2024-09-28 00:11:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff7061bf-2a7b-3c5e-bf20-9f3ebab258db | -19.216101 | -43.697601 | 2024-09-28 00:11:04 | METOP-B | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30972e76-4c59-3b6e-82fb-bbbeec7222bf | -19.2178 | -43.706501 | 2024-09-28 00:11:04 | METOP-B | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 00ce3156-07ff-351a-a2a4-a08928538c21 | -19.219601 | -43.715302 | 2024-09-28 00:11:04 | METOP-B | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 384b2091-b63f-305d-a67a-b22c55a28f33 | -19.093599 | -43.442902 | 2024-09-28 00:11:05 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ee924a6-d23f-38ea-acb8-5ab714a94ba4 | -18.697701 | -42.063599 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ede3a9d3-71d8-38d3-876f-b68f0b3daec3 | -18.6992 | -42.071201 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c46704c0-02f6-36fe-93ee-36f06525f8a3 | -18.7008 | -42.078701 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3102a13c-bf10-3f4a-ae61-f9765b2f51c8 | -18.6894 | -42.073399 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f90ee4c1-55f9-3c7b-8dda-8569a8ed2143 | -18.691 | -42.080898 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 831e554a-8910-3614-9399-40e78852bd69 | -18.6926 | -42.088501 | 2024-09-28 00:11:07 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f765b67-dd02-391a-9ff4-9cb965d7ef54 | -18.4869 | -42.183399 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 479beceb-837c-3894-9dda-fac4d4e6670a | -18.488501 | -42.191002 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2fd79eb9-705e-3ebb-bb7b-880ff538b261 | -18.490101 | -42.198601 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7541b7e0-3510-311f-b4c9-f0951832a02b | -18.491699 | -42.2062 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc7328e4-9872-3e98-a665-a39685a09203 | -18.493299 | -42.213799 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e68b4ab-1140-3e62-8269-ee12ff4ddd4b | -18.4949 | -42.2215 | 2024-09-28 00:11:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a10ebc38-c8e1-3206-8734-39b1a8dd5431 | -18.4755 | -42.178001 | 2024-09-28 00:11:11 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 236c629c-f9c0-33d9-a6aa-b65b802c0786 | -18.4771 | -42.1856 | 2024-09-28 00:11:11 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7295e4c2-e207-3b12-8b6c-55152ada6216 | -18.478701 | -42.193199 | 2024-09-28 00:11:11 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ac1b593-b741-30e9-86cf-8c9eb63003f5 | -18.480301 | -42.200802 | 2024-09-28 00:11:11 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6d3bacc-02e8-3e12-a286-0b18f3201b19 | -18.481899 | -42.208401 | 2024-09-28 00:11:11 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ac1bdb7-12ff-3c0b-8843-5355ea5fac32 | -18.341801 | -42.176601 | 2024-09-28 00:11:13 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| acd6b6a6-b383-32ef-a781-ae7a67a0bf8f | -18.515499 | -43.013901 | 2024-09-28 00:11:13 | METOP-B | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cb42177-36d1-3b09-9d22-01c8b81c5a01 | -18.328899 | -42.163799 | 2024-09-28 00:11:13 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3686244b-b076-31a4-96c4-7a5175831531 | -18.602699 | -43.391399 | 2024-09-28 00:11:13 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbf1bcce-738c-3213-ad39-ffd848d3f9a7 | -18.6045 | -43.399799 | 2024-09-28 00:11:13 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5eb83df7-4ecd-3c23-a324-8422546f2a4e | -18.387699 | -42.791 | 2024-09-28 00:11:14 | METOP-B | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2069248a-685c-3ff6-a204-20afa304fa8b | -18.281799 | -42.1348 | 2024-09-28 00:11:14 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7aac4ff3-29b5-3d8b-abd8-0a72ce2e77bc | -18.2834 | -42.142399 | 2024-09-28 00:11:14 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbfba874-5c26-36ca-898a-66a88a4591e9 | -18.285 | -42.149899 | 2024-09-28 00:11:14 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 362b465f-8105-3295-9dd3-e4a5a6f673e0 | -18.252399 | -42.141499 | 2024-09-28 00:11:14 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c65342f0-5d7e-3db9-a031-6dcbca223922 | -18.386101 | -42.783001 | 2024-09-28 00:11:14 | METOP-B | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 077b1f3f-294c-3d22-9e89-f53f0586bf48 | -18.358299 | -42.747799 | 2024-09-28 00:11:14 | METOP-B | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bb4432f-3e47-340f-94d1-83a59ec0a22e | -18.360001 | -42.755699 | 2024-09-28 00:11:14 | METOP-B | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25a736d4-42da-3b40-993e-a6affcda58e6 | -18.2917 | -42.525299 | 2024-09-28 00:11:15 | METOP-B | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e2ccd1c-1ad1-3a9c-825f-a43daa44afdd | -18.293301 | -42.5331 | 2024-09-28 00:11:15 | METOP-B | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c87993b7-9e3c-3413-ae21-20938be99d10 | -17.774401 | -40.446098 | 2024-09-28 00:11:16 | METOP-B | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18679c14-228d-3d1f-ba8c-06179204c406 | -18.142099 | -42.3978 | 2024-09-28 00:11:17 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa48f27d-a454-392d-be7c-1daf640d65d9 | -18.130699 | -42.392399 | 2024-09-28 00:11:17 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9cb0431-987e-33bd-9aaf-2dadffbb69e2 | -18.132299 | -42.400002 | 2024-09-28 00:11:17 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7adba763-c7d7-3a82-8a6e-e7b6c370a634 | -18.1339 | -42.4077 | 2024-09-28 00:11:17 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cbd4387-347d-340e-aca2-3b3253b8e1b9 | -18.3682 | -44.002499 | 2024-09-28 00:11:18 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd4516b-13ff-3404-a3e2-e273301f31fd | -17.976299 | -42.291698 | 2024-09-28 00:11:19 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebe6390d-5c59-35ed-896c-ae5f2c2ac24a | -18.8295 | -46.6605 | 2024-09-28 00:11:19 | METOP-B | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c73a3cda-3939-3217-a799-a29cf1506edf | -18.8319 | -46.673401 | 2024-09-28 00:11:19 | METOP-B | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 106cfc96-da63-328a-9611-61a8fa1f72c0 | -17.9104 | -42.125 | 2024-09-28 00:11:20 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87744875-6e79-3ee3-ab9f-701055d27044 | -17.9119 | -42.1325 | 2024-09-28 00:11:20 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b345d050-0dd1-3471-af06-61c58d8aae97 | -17.8794 | -42.124199 | 2024-09-28 00:11:20 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a030f73e-dcf5-3c53-9947-fecb04a0dc17 | -17.881001 | -42.131699 | 2024-09-28 00:11:20 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac127e6c-70ce-3948-b204-4f8cdb7ec119 | -17.308001 | -40.293098 | 2024-09-28 00:11:23 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b64473a-4bb8-39fd-9f8f-2f9adb76bb6a | -17.309601 | -40.300301 | 2024-09-28 00:11:23 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7146ab9-03a4-3802-8d40-1399ab2e5d2e | -17.311199 | -40.3074 | 2024-09-28 00:11:23 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ba64076-6449-3b52-a986-eb5b66404a5b | -17.715401 | -42.319302 | 2024-09-28 00:11:23 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47879e5f-df35-31f2-a53e-a726605efe66 | -17.705601 | -42.321499 | 2024-09-28 00:11:24 | METOP-B | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e972586f-c569-3c58-a35b-b680d51e03f7 | -17.7964 | -43.250099 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08714dc1-a397-35b8-b5b0-bbad5fb82f14 | -17.7981 | -43.258202 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5a2087-8ff4-3759-8db6-5760ac0a7db4 | -17.7997 | -43.266399 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30adcd05-28f6-311a-ba9b-b089a5bceaa4 | -17.801399 | -43.274502 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 204feabb-a768-380b-b6a8-3503ddc51ecf | -17.8048 | -43.290798 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 76603377-3a05-3411-93dc-935cf148b48e | -17.7866 | -43.2523 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bfd83aa1-3417-3b43-b5aa-6bf546b94f99 | -17.7883 | -43.260399 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79467c9a-a87a-3656-adb5-de95de40ff79 | -17.7899 | -43.2686 | 2024-09-28 00:11:25 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
