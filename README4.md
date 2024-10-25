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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee607d78-450d-3d87-a5d8-eb636c8d3e97 | -12.89839 | -45.06033 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4dccac96-15b4-35e8-bcf7-b105eaf8406d | -12.58921 | -43.83535 | 2024-10-25 00:26:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 9d2e597d-1eeb-3706-b442-bf3c211d103f | -12.58243 | -43.84253 | 2024-10-25 00:26:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a2331fd5-68cb-35b9-afd4-728a7668daec | -12.5808 | -43.82994 | 2024-10-25 00:26:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a74b2ccd-be85-36b7-9fa2-9d5dcc55d103 | -12.57887 | -43.83678 | 2024-10-25 00:26:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 18ebb8b2-fa32-3d51-ba6a-492f7c2e6eb5 | -12.34803 | -38.06654 | 2024-10-25 00:26:00 | TERRA_M-M | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| c3ed0a9b-dc0d-328f-989e-cfe82e5859cf | -12.34652 | -38.05648 | 2024-10-25 00:26:00 | TERRA_M-M | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| fb3af261-e270-38de-a768-f061e7c53467 | -12.34104 | -38.06361 | 2024-10-25 00:26:00 | TERRA_M-M | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c1796764-4086-3395-a57a-1b6e7a09d37c | -12.31154 | -43.56706 | 2024-10-25 00:26:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2cbcd4a-694b-3a24-96ec-d964138ae329 | -12.30143 | -43.56839 | 2024-10-25 00:26:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6736ec61-66ae-319f-9203-a070ad75e6ae | -11.89757 | -43.83707 | 2024-10-25 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8e95bfd4-5d6d-35e3-b7f6-224b444cafdc | -11.67882 | -41.13597 | 2024-10-25 00:26:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 88cb6da4-54a2-378c-86b9-1e6b053c7b00 | -11.58009 | -43.97884 | 2024-10-25 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e980b10c-1512-338f-81f3-14bdd22bc303 | -11.54048 | -43.99671 | 2024-10-25 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6168fbc2-5b8b-33da-bc15-159ebcf272b7 | -11.5389 | -43.98432 | 2024-10-25 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 70289059-a9da-3d18-8ee5-01ca0236fac6 | -11.48323 | -43.24146 | 2024-10-25 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 889893d9-9b0f-38a2-9647-2288a570a950 | -11.48177 | -43.23038 | 2024-10-25 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 516f992e-1a83-3e81-a9fa-5b2c0122cf42 | -11.26851 | -45.02887 | 2024-10-25 00:26:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7cf3dbeb-0010-35f5-972e-89936289fc88 | -10.89954 | -44.3091 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c89608d-30c1-3d90-9627-696f4f690ebe | -10.87511 | -44.79549 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3b7f0aaa-8a65-34e5-834f-44db76c49785 | -10.87344 | -44.78192 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d8e5488f-a683-3419-bde1-0763e367fecb | -10.87233 | -44.8021 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a61880df-c000-373e-979f-4b6cc5ab8fce | -10.87055 | -44.78842 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| a2026c36-a8be-3f4a-99ff-da1b0b41ab1f | -10.86429 | -44.79689 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d34b6595-3229-38b5-a6a4-20780b379bed | -10.77058 | -44.26778 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9fdc8259-cb2a-3e25-a239-7319983a97ba | -10.76896 | -44.25525 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e3eb89e0-73a7-34fd-aa13-a37bbf7d0a53 | -10.62826 | -36.93887 | 2024-10-25 00:26:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| cc62805d-ee38-3045-902b-52c4f155bd48 | -10.62641 | -36.92682 | 2024-10-25 00:26:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 5a22448d-1307-362c-9660-e9b6af3f4d94 | -10.58984 | -44.28979 | 2024-10-25 00:26:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6e3ffae6-459f-354f-9a62-fdcbd7fb5f9e | -10.57946 | -44.29115 | 2024-10-25 00:26:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 84ce86c3-dcc4-303e-9149-24d5efd81dd5 | -10.51509 | -42.4027 | 2024-10-25 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bd681285-ec15-3272-b440-035e8496a819 | -10.51377 | -42.39289 | 2024-10-25 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 26f47a4c-106a-336b-9ebd-e482df79623a | -10.47738 | -44.21085 | 2024-10-25 00:26:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 030dc331-7466-3f36-afe5-217d2ec07f7f | -10.09129 | -36.3054 | 2024-10-25 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 5e6f48a3-d144-37de-9761-4dd3a13ef14e | -10.08913 | -36.29142 | 2024-10-25 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| 379b3a49-1c7e-3300-956b-1e3837e67157 | -10.08236 | -44.79039 | 2024-10-25 00:26:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2e69dfbe-43cc-3b6d-921b-2c393aa1f770 | -9.57844 | -49.64377 | 2024-10-25 00:26:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d96829ab-6f6e-304c-81f2-05d3ec731c85 | -9.44479 | -48.88676 | 2024-10-25 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 04144018-036f-3563-93d0-655f409c79d4 | -9.44425 | -48.89244 | 2024-10-25 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 952fd24c-3be6-3af9-9275-ec45a70ecaaf | -9.43016 | -48.88926 | 2024-10-25 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d545c498-12da-3aff-91e8-1c227fcf8e31 | -9.42962 | -48.89491 | 2024-10-25 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 472c54e4-6a60-3362-8798-e6d023cc25d1 | -9.26888 | -46.23068 | 2024-10-25 00:26:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| db170a22-507e-30d5-a502-516014d1855e | -9.26778 | -47.91021 | 2024-10-25 00:26:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 4cbc4b7f-4e63-3abd-a5dd-43f4fe6e9e3b | -9.26675 | -46.2138 | 2024-10-25 00:26:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c82250ee-ca70-3224-8639-a87a57a7b122 | -9.07409 | -47.99892 | 2024-10-25 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 08089088-efc6-317e-905c-a2eae39792d7 | -9.06779 | -47.99296 | 2024-10-25 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 50686dbc-c687-312b-b5cf-4e516c54967c | -8.97984 | -48.81728 | 2024-10-25 00:26:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 1d685546-8ea9-39d8-a0cf-4a62ee75b051 | -8.96072 | -47.63386 | 2024-10-25 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d9c777a3-25fd-3321-bfc6-197f9c88ca44 | -8.95076 | -47.64069 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 03c368c3-f0d6-3318-9be8-3a138c1fb9a4 | -8.90519 | -48.56468 | 2024-10-25 00:26:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 74f7a3fc-2c1a-3daf-90eb-3aa608aa79c0 | -8.90217 | -48.53977 | 2024-10-25 00:26:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 1090a5a1-70d4-36b0-ae80-62320c005e0d | -8.81412 | -47.92888 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a3269143-03c9-3e11-9776-9c87961304d1 | -8.68539 | -50.03712 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| bdc85832-b2dd-3d54-b48f-bb678e12c776 | -8.67626 | -50.04366 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 36ac51f4-5375-3f62-85b8-cdb25d69c093 | -8.57583 | -49.22797 | 2024-10-25 00:26:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 261d278d-f7d0-3bb3-bb62-5f8812dfd64e | -8.54155 | -49.56105 | 2024-10-25 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 608f3e8f-eeb3-36c3-bbd2-4aa79ef4d731 | -8.53867 | -49.55481 | 2024-10-25 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 966d6eee-c5a4-367d-a105-2a1cd903de34 | -8.51425 | -45.87766 | 2024-10-25 00:26:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6ea98a6a-4606-3f38-aea5-2e1e5bbe030d | -8.29291 | -46.47449 | 2024-10-25 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 29190f1b-bf7a-34ae-a18b-7d4240bc8ba2 | -8.02088 | -49.6533 | 2024-10-25 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 266715b2-45db-316c-8286-3e2d10e23b2b | -8.01998 | -49.63033 | 2024-10-25 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 77848a9a-2be5-3514-a90f-90510e07bba0 | -8.01735 | -49.6238 | 2024-10-25 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 2697634c-3bba-3dd2-95a2-dc3f79f8a64c | -7.89998 | -46.69394 | 2024-10-25 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b8d6767f-4025-333b-a97c-df50308d4e00 | -7.89318 | -46.68939 | 2024-10-25 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 54f7637f-5dc7-3c84-8c44-87fdf344b5db | -7.53748 | -45.85532 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a82888e4-ecd5-3657-8fec-6e6edb7a0d00 | -7.53563 | -45.84079 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ea97908c-934c-330a-ae0c-8af1ca52f6be | -7.43214 | -46.6583 | 2024-10-25 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3d2cac77-c1c5-3545-a86a-ab2ce458de42 | -7.33879 | -49.15648 | 2024-10-25 00:26:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 381855f8-c294-3134-b90b-141d4ec03800 | -7.33552 | -49.13007 | 2024-10-25 00:26:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 90a56366-954d-3866-86f3-603243501375 | -7.26661 | -46.06532 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 27c1946c-55f0-3a99-898a-8f8f9796f4b9 | -7.26567 | -46.05967 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a222a51e-a451-37c4-afbf-29145ed1e20f | -7.26462 | -46.05047 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5cdbf4b2-3b53-363c-9795-300f4c27da88 | -7.26379 | -46.04482 | 2024-10-25 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5d9a4331-7571-31e4-a930-3e862ff4e904 | -7.21843 | -45.59888 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 21ba80fe-a64e-30ee-84f8-17eff33b6a0d | -7.21667 | -45.5851 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b7ca42db-2d69-3b4d-ad53-c134bc159e81 | -7.21418 | -45.59133 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d42fc7ca-a5c0-3e92-ae9a-bec2cec6fb37 | -7.21233 | -45.57763 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 351ae0f3-ac89-35b2-87bb-3c445cb56222 | -7.19715 | -44.72202 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9ffa5813-d896-3bbf-86a5-4dd4b84ee38d | -7.14224 | -44.84584 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2d7c5c0b-c2d5-3fbd-b0e6-a566c1600c0c | -7.04741 | -46.32224 | 2024-10-25 00:26:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ab386851-528b-3a9f-8ac0-e5c670b7da84 | -6.84467 | -44.75638 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6d4afc8-33c6-39af-acf5-b0ed6b71d718 | -6.83455 | -44.75798 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a22a45a6-2f87-3312-aab2-5483895622b7 | -12.60993 | -48.51049 | 2024-10-25 00:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 08bf72a7-2284-35ea-8020-8f3299386fc1 | -12.60905 | -48.50397 | 2024-10-25 00:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e1a13335-651f-3cc4-8d6c-2550579e5999 | -12.54235 | -48.72541 | 2024-10-25 00:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 0aeef574-0981-3a4f-97bd-ba3200130cf6 | -12.50268 | -47.30007 | 2024-10-25 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 29259e9e-9729-3d6e-b29c-3abc0fdae187 | -12.18059 | -46.99678 | 2024-10-25 00:26:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| af49795e-2a69-39ec-a5ca-2f02168c5858 | -11.77448 | -47.07652 | 2024-10-25 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| eccdac72-ba80-3204-bf6f-aa5402b1310c | -11.70026 | -47.12948 | 2024-10-25 00:26:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c03e6e42-d0c0-3dad-89b9-1424d2c2fd23 | -11.69052 | -47.13712 | 2024-10-25 00:26:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dccbb64a-89ae-3858-a25d-b83be716aafd | -11.63854 | -48.48442 | 2024-10-25 00:26:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 346f573c-1149-3abd-ab89-a729df8f1d9a | -11.63541 | -48.45712 | 2024-10-25 00:26:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 6867cdf8-19fb-372d-9366-423650650dc4 | -11.5477 | -49.28252 | 2024-10-25 00:26:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e9b94ba1-11f6-322b-90f7-7e1bd2abb6f6 | -11.42189 | -47.81746 | 2024-10-25 00:26:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3c870374-b393-36d7-8f60-c1d67cd0c9f4 | -11.04156 | -49.47442 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 3188cd21-1ebe-3ca1-a899-6eb4b5a22907 | -10.8823 | -49.15023 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| dc3b1023-b243-37f0-a0c6-1cb10d071dc7 | -10.86759 | -49.53943 | 2024-10-25 00:26:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9495bc39-262c-30ba-ae03-35de51edcb74 | -10.68268 | -49.12514 | 2024-10-25 00:26:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a7eef99c-e857-3f79-800b-58882129cc12 | -10.68181 | -49.10152 | 2024-10-25 00:26:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 10d181fb-9366-3bfd-a039-3006f66e5bc0 | -10.65025 | -47.93011 | 2024-10-25 00:26:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |


[Clique aqui para ver as próximas entradas](README5.md)
