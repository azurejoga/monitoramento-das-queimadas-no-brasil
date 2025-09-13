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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b14cde0c-88ae-37a7-9634-d787144371fb | -15.46616 | -47.3375 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc5c4a60-70cb-3aa6-873c-5660aef5a562 | -21.61415 | -46.81419 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6ee67229-03eb-3ada-8e4c-0940c65887a5 | -21.6706 | -45.39339 | 2025-09-13 03:49:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb2f1089-e623-3d6b-b8f6-aa1371e65243 | -22.18157 | -49.61359 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e70be504-90a8-3196-b551-1af6800992ba | -22.54573 | -47.37148 | 2025-09-13 03:49:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54a3ef94-960b-382e-b590-731365d0a962 | -16.37081 | -41.38387 | 2025-09-13 03:49:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7cff77ee-5c2f-37ab-b3ee-977e3b6f9caa | -14.61564 | -46.33872 | 2025-09-13 03:49:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21bbb197-edd9-3b1c-a93c-7ce5dd9ff7b2 | -15.68832 | -50.58002 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75a8e631-c43c-363d-b080-68581929671b | -21.58768 | -48.42321 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 754b02a9-21a3-3aa0-94df-3e0fa768da98 | -15.60714 | -47.92794 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5a737ac7-e684-3cfa-a4c5-65cd3c43dfd1 | -21.30203 | -44.93864 | 2025-09-13 03:49:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3d91f6b-56dd-305c-9fe0-4bdecbcd9d52 | -21.58105 | -48.42133 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d8ca83a9-57a4-3671-8f95-01be31dc986d | -17.3616 | -42.70817 | 2025-09-13 03:49:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 82ff45c9-1bfc-3550-aae5-8ac2536a571c | -16.409 | -49.04389 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf9d24a0-3dff-3ce9-a3f5-16ceafb8790b | -16.32614 | -43.75876 | 2025-09-13 03:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6fda2db-ae25-3cde-83b2-5ffcceaaa659 | -15.863 | -47.23553 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ed311bd-9c5b-3459-bc7a-6771ab857e1b | -14.43133 | -48.43554 | 2025-09-13 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c3b38b5-8785-33a6-aced-ffb2f4ffc1e8 | -14.43522 | -47.33994 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36f76525-304c-3dd9-a1c4-d08165b0849e | -22.57177 | -53.03969 | 2025-09-13 03:49:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f518558-94f7-3e0a-97f6-c3039448a28d | -15.86331 | -47.2328 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c29772b-f691-30a4-9c9a-b934ac5246c2 | -15.70819 | -50.58515 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a00dbc07-ce80-3eee-8882-ca59702e5850 | -21.58255 | -48.41459 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| edfb6f70-dd73-3d6e-bb5a-607191ec9d23 | -17.39312 | -43.52743 | 2025-09-13 03:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dd5d415-c512-3c03-8d5f-f2cebbc29b39 | -14.43754 | -48.44083 | 2025-09-13 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf5d5a1-ad4f-32f6-9b82-4c87aa1b64df | -22.22709 | -48.60223 | 2025-09-13 03:49:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0a3fa082-6748-3f90-8c6e-136f70125be4 | -21.32422 | -44.99345 | 2025-09-13 03:49:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff29bb63-d765-3c72-8fe5-da476a2df81f | -21.54926 | -48.79111 | 2025-09-13 03:49:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f055e16-6d59-3130-a883-f0ad746b86a5 | -20.60899 | -50.40239 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71f2ea3f-de64-3583-948c-d29cd8492781 | -22.57333 | -53.0336 | 2025-09-13 03:49:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7363fa40-9dc6-3c19-a59d-205f7d93e797 | -20.59581 | -50.40486 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 685b130a-5987-312b-b451-657e83c6df5e | -21.93401 | -47.57006 | 2025-09-13 03:49:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8feaa2d-c649-3819-b719-1381a9dd1e2c | -20.37271 | -50.12793 | 2025-09-13 03:49:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3b58eb2-fb20-353a-8e52-688cf2b2eb8e | -15.68963 | -50.57406 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71a1c8c1-7831-3798-ae85-1ef393cb64be | -17.71556 | -40.27097 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8854cc54-8c8c-3dc8-b3ab-88c9325605ff | -16.25838 | -50.07029 | 2025-09-13 03:49:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b38a22c-2cd7-3f35-ab37-bc3200e5e4c7 | -15.45523 | -47.33453 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a047c62d-fbd0-372b-89ab-9c0d7f196307 | -16.08884 | -49.95308 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83bad110-33e2-3be2-b711-7c534c0571e7 | -21.61401 | -46.80975 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0535df8c-7f22-3752-bee2-b1f3d5ac1882 | -22.66046 | -53.11901 | 2025-09-13 03:49:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2bde76c2-15c2-3b0e-9add-eb67911cc33d | -17.38895 | -43.52656 | 2025-09-13 03:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d488faf7-7361-3735-9884-f8377cf283f4 | -21.61026 | -46.80388 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 18568479-18de-3190-ba10-342713754f23 | -17.35763 | -42.70731 | 2025-09-13 03:49:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0a2ec366-7026-3376-989b-db428df74de4 | -15.23863 | -44.06271 | 2025-09-13 03:49:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39deb833-a2d6-348c-9007-667a65bfa4dc | -21.60912 | -46.8093 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce621bfa-b9e1-3059-9880-100c18a9a685 | -16.06073 | -50.01213 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 618b1c18-cf65-302e-8854-ab26897ae83a | -21.61515 | -46.8043 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 44827d62-5651-389f-a9a4-7bdf2fcb9aca | -25.51426 | -49.11231 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0fe6833b-c77d-3b15-92aa-84d5f065bdcb | -21.63176 | -46.79634 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d0749a53-6eb5-36e8-87cc-a5a17351ddea | -23.27547 | -47.52284 | 2025-09-13 03:49:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0834f03a-2074-3d64-951e-5a5d09bd7a81 | -16.4162 | -49.24666 | 2025-09-13 03:49:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d37a55c7-5a05-3510-a701-41789eb881ed | -16.08556 | -49.96786 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| edcdd6a3-2aa7-30ed-b659-5a5e6422f150 | -15.84792 | -49.94232 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03dd9541-c988-3b0f-a9e8-d7e69c185a7f | -15.71067 | -50.58609 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0a59fa48-334f-3e10-832d-852e677e096f | -17.35151 | -42.62854 | 2025-09-13 03:49:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 418154a9-2f65-3594-8129-17d2434f8881 | -21.61524 | -46.80882 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 737f24db-8c20-345d-ad2f-14c1e3c35122 | -15.54165 | -47.95505 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d71ae10e-b07a-3a91-a61b-344d2d5780f5 | -15.16023 | -50.1617 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 081a3afb-ef44-356b-94b1-f9d5f07e5374 | -21.61145 | -46.80304 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a0f3f783-82f8-37f5-82c4-a882d8725ca7 | -16.28692 | -45.68133 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e09a6cb8-584a-3bec-a49c-586a857e7df0 | -16.08129 | -49.95686 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dcd1fff8-2d43-3365-9a79-e3776832c731 | -16.41608 | -49.04035 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1e688bb-611c-3e1a-ba58-f3aae17cf181 | -21.87047 | -46.50104 | 2025-09-13 03:49:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b366c148-0149-3cf7-a203-1bded679a7f9 | -21.6129 | -46.81498 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4b21efde-5533-3e79-a175-1ed824fdba5c | -16.24826 | -39.02803 | 2025-09-13 03:49:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b026ced3-1866-36a1-ba20-a09142d41c72 | -15.71476 | -50.58712 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 26ad658f-f74e-3549-ae7f-a9a536fc7626 | -23.45928 | -47.35332 | 2025-09-13 03:49:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f151210-9bff-3329-8836-f11c8446dcac | -16.65786 | -40.8414 | 2025-09-13 03:49:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ac14a934-52d9-3b5f-b1c0-59c206d315e2 | -21.62959 | -46.80666 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6dafa7fa-6208-3087-9712-80ce9243dfa2 | -20.64928 | -48.69696 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 201d35d1-66d5-33db-a65a-c1bc4d68c63b | -16.0702 | -50.0068 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 42fea7de-cff5-3755-85e4-d3a6cfb21ed4 | -20.65016 | -48.69302 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 196ba593-c3cb-3ae6-bf04-f461ee92ccfb | -15.46148 | -47.3322 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec910144-8a4b-3f38-96fe-3be29a3cedba | -15.46701 | -47.3334 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d55ee96-f89f-3791-95b6-91a80902801a | -16.27962 | -45.68406 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 248c9a48-2579-3db6-a380-6027390dd824 | -16.08329 | -49.97812 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c24c33b-1497-38f5-8be0-e1a1424b3209 | -21.61732 | -46.79863 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5bbcb0f4-d2ab-3f33-89f7-e41887de675a | -15.53779 | -42.57372 | 2025-09-13 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb56124-6f1c-30f0-b443-17e5d1af4d3f | -23.80974 | -50.09341 | 2025-09-13 03:49:00 | NPP-375D | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 04c51581-f642-3561-8828-f12a97610e7f | -20.4223 | -50.74573 | 2025-09-13 03:49:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a27daa72-3b13-350d-9719-75f43a56da75 | -21.62589 | -46.80058 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| edb211f8-c37d-3434-ab85-5bd7af175baa | -17.37424 | -41.71413 | 2025-09-13 03:49:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ea4ce93-10ab-3d55-9b4f-cd9ff12b7dc4 | -21.58623 | -48.4229 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0837f51-2184-3205-bff2-498a4307e668 | -15.69367 | -50.5875 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b33af392-aafe-3cf2-a2c7-78bfe24b64d6 | -22.18386 | -49.61532 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 73bd2472-7d3f-3abc-b104-1138e0611dbd | -22.22632 | -48.60569 | 2025-09-13 03:49:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ab9dcb6d-dd92-3cc9-8407-9cc6d6e87cb9 | -21.58547 | -48.42632 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 30340004-90a0-36a4-989a-d0a92d5ede93 | -16.05952 | -50.01773 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 844bdf86-fc63-3ceb-be74-fa5b106d7656 | -21.58248 | -48.42168 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fce7a646-071f-39b0-b21b-14a293b5fd60 | -20.37164 | -50.13258 | 2025-09-13 03:49:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d564387b-ad88-37dd-a4d8-b516691b3e59 | -21.55831 | -45.43402 | 2025-09-13 03:49:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41cc78b6-5447-3b1c-84df-8efbdaa94a33 | -15.85366 | -47.2255 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a9e273-ba9c-3a86-8de7-2015145d052f | -17.71974 | -40.26759 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2415097b-9170-3550-9826-2cc2adeb93d9 | -20.59481 | -50.40891 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc056639-bbbd-3963-ac46-2c128100a8a0 | -16.64885 | -44.9338 | 2025-09-13 03:49:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 720e65d4-f996-376e-a15b-c37851dcb126 | -23.61154 | -51.38352 | 2025-09-13 03:49:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cbd7ac76-de7e-3baa-89c6-907133ac01c2 | -17.35053 | -42.6339 | 2025-09-13 03:49:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 79a93127-f423-3a11-9fd9-d8ce8be0f4af | -15.16155 | -50.15574 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fde017b-8c75-3465-9007-53a4a0a0de48 | -17.71343 | -40.26222 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 948176a1-cb23-38d5-93c5-c9b0d1e2fb60 | -15.23407 | -44.03773 | 2025-09-13 03:49:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a0e2af5-1d7a-302b-bd18-250892c27be5 | -23.13563 | -49.65781 | 2025-09-13 03:49:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README38.md)
