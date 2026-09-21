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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bdf6c8c-7eed-38d5-aeaa-85d47b850e31 | -4.26246 | -55.77406 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdbfb01e-0a30-35ab-97b1-03163557571f | -3.4937 | -59.60823 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cce843bc-9ace-3160-b23b-1d8d282cf1c8 | -3.17966 | -59.70007 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26673cdb-14d6-388b-8bbb-d231ed6b19de | -2.86809 | -57.80961 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cbfc69fe-935d-3072-a8cd-8ab3d0beda09 | -4.52831 | -54.97538 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47afe851-2f32-333f-a8d5-22c8f3f80ad0 | -3.82477 | -59.3276 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77174413-b387-3228-bed8-4dfee99f3e04 | -3.05364 | -61.26964 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c770de0-cf17-3fe6-adfb-f21790f40419 | -2.87411 | -57.81943 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54a957b9-8bbe-34ba-bd8a-286080583af7 | -3.68444 | -59.03088 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fccaba66-4182-32e4-a074-f037fe7806e7 | -3.1315 | -61.39851 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dae526d5-e68a-3f03-b725-e270143d006f | -4.41258 | -55.24493 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 388cd70d-9cda-33cb-ad0c-5cc3eb3f9c7f | -3.3963 | -59.58616 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a9578b0-4812-3346-ac9e-b583eeca2436 | -3.4834 | -59.60662 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 794cb4b0-0eea-30fa-b6af-e8d1e2842258 | -3.60373 | -59.01539 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c01ea6-443e-3b7e-a3f2-09d682584d37 | -3.77091 | -56.79293 | 2026-09-21 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e5ac910-f385-33d9-86d7-fd8d865b9880 | -3.64459 | -58.86905 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ae9b55e-6f26-35bf-8839-56488138faa2 | -3.48973 | -59.56585 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a740def6-39f4-3ed3-9f23-f1299b07faeb | -2.17495 | -48.32021 | 2026-09-21 05:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2843289b-b5be-358f-9248-aee0daab60f5 | -2.99904 | -60.8031 | 2026-09-21 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 990e1597-7299-3b07-92ce-919aa6a925d2 | -3.30398 | -57.86706 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88760abc-97b8-373e-a90f-de1c632de14b | -3.44811 | -57.90515 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e21d5d-943b-3485-9518-d07d0f49ef65 | -3.68852 | -60.57092 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7947a89-34a9-396d-8d7a-4d24c082330f | -3.73676 | -51.82087 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97bc4aad-a2b5-3085-b320-62bdddbe28de | -3.44069 | -50.60107 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 400e83cc-cf59-3620-9e69-99a2fa1e3ae2 | -3.44413 | -59.09486 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc0ddf5-7bef-3c6f-b6b0-04238cee8d5a | -3.50575 | -59.93257 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64dc660-26f4-3197-a47b-fbb12cc4bd6a | -2.61681 | -51.72719 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c47a8ac-d649-3023-9fe2-75a99a58d3d1 | -3.82009 | -59.33468 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ba641bf-40e9-3815-92c7-f8909c5d34c2 | -2.64253 | -54.69226 | 2026-09-21 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 887fa6bc-748d-3bf0-a988-432533565796 | 1.38529 | -50.9267 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb601e8a-65d7-3609-8ac2-e453373c076e | -3.45135 | -50.61177 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8914ac5e-57ae-310c-aff0-7411cb54eaf4 | -3.45847 | -58.2216 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e001b5e5-da67-36db-8a09-1b375246961c | -3.18307 | -59.70061 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51dd723e-ecc9-31a7-9ba1-413f732a6ff1 | -3.66303 | -54.26485 | 2026-09-21 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 225cac08-56a5-36de-a46c-dc42b90e76bb | -3.48687 | -59.56161 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f4078a6-1487-316a-b77e-f5c48f57afa8 | -3.18778 | -57.87363 | 2026-09-21 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b0fbd34-cef0-3a54-bf73-a44c3111f465 | -3.07194 | -61.28313 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05191d50-6b7f-3948-abc5-e405424a0256 | -3.66091 | -58.57598 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba5b690-1cfd-325c-b114-8a7889ca653d | 0.25983 | -51.00117 | 2026-09-21 05:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 230dd1e0-9bf2-3a21-afea-d6f7bf97063e | -3.43935 | -50.60983 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 685f23a3-2e00-3103-afdf-507ad09ab791 | -3.19351 | -60.42923 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd1f23f3-c35a-3c14-95ca-beb0d2bddd44 | -2.87702 | -57.78654 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8babfa1-05f6-36c2-8716-07bbac4f3202 | -3.05087 | -61.26566 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3e35742-1cee-397f-87c5-7322f7e8565d | -3.30028 | -57.86649 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cfef99a-241e-3df3-9775-9a89e5094fae | -3.796 | -59.70707 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c074b0c-ef4a-362d-a2cd-921eb3796a4b | -3.90104 | -60.5964 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d79d9f67-749a-37f0-80c4-4afe08a588f7 | -3.68966 | -60.58552 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa0a5879-3d16-3b9d-8933-eec16818321b | -3.49089 | -59.55841 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0d26f2-af91-3e09-99a2-42eb6732880c | -3.45053 | -58.39541 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 51640805-e013-3358-9446-14fb180ef5f2 | -3.40451 | -61.29973 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19a9a857-8b55-3f98-b479-acc25ec0d68f | -3.78234 | -51.92355 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38db68ea-52aa-3444-a811-4238fc65d8e9 | -3.73418 | -59.40676 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c2dbdb-7129-3057-8cb4-a26172332096 | -3.05309 | -61.27309 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38e22212-5e23-3f50-9663-7310b6bb8e9f | -3.46371 | -58.40593 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a03567e-f6ab-337b-967b-5c865516d262 | -3.38843 | -61.29367 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe3c6a71-0beb-3475-8ad3-3d8c1ef3f175 | -3.43264 | -59.26158 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f94abb4b-6bd4-3a20-bcc0-97d062c3a345 | -4.34564 | -55.65908 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ea78def-f51a-387f-a112-5c48c9c1f3b9 | -3.45647 | -58.21371 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a967eb2-bccc-32e8-9b42-f86ee53cfe20 | 1.76982 | -60.23465 | 2026-09-21 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d82cad5-5baf-317b-9891-b63d9169a229 | -3.39101 | -50.43747 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02858f1f-502c-3023-ac5e-e8c28ac7624e | -3.42917 | -59.26104 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c64d676c-5420-3f68-ba10-caa17ec09cf6 | -4.35118 | -55.65176 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03ea4f2e-5987-30bb-9ccc-a64246793907 | -3.39646 | -50.4426 | 2026-09-21 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e1a5502-0060-3289-8486-a375ef432717 | -1.77883 | -60.08714 | 2026-09-21 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3c597f9f-cc66-379b-9842-7b69a5723f23 | 2.31808 | -60.91776 | 2026-09-21 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c8ed40-3866-363b-9919-d2bfb76dd76e | 0.78526 | -59.20658 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9e33286-2598-3adf-ae32-4c3e68da913a | -3.68409 | -60.59906 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dc2b3ba-678c-3797-9faf-0dac874180a9 | -2.91857 | -54.19339 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 861f4f1c-4e1f-32e4-9c2d-69614f56dd15 | -3.73071 | -59.40623 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b24726b4-faa7-3a5a-bfb1-0fba68c929ea | -3.39356 | -61.06763 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6b9d4b8-bd78-33c0-a74e-9f596e2f889f | -4.18659 | -59.9543 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f17479ae-3cba-3c24-bee1-7aba248c142d | 1.74189 | -60.57111 | 2026-09-21 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea805373-1fc2-34a7-bea9-e5e8ff968272 | -3.17269 | -51.3552 | 2026-09-21 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4fbd007-b1d5-307b-8f7a-8bb660f78ec1 | -3.20078 | -60.42675 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f315fb0-39ec-30c0-8243-81495fed662c | -2.87247 | -57.80582 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b4af468f-814e-3189-8480-b33a8328cf69 | -3.04918 | -61.25478 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1433dc8-3a62-3113-af39-7c17366deb50 | -3.04754 | -61.26514 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dab6646b-7019-328b-92f8-127b760abeff | -2.60449 | -59.76144 | 2026-09-21 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b14ca12-5d8d-325a-92b9-1f92ae2dda81 | -3.3408 | -61.29328 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc0ff34-3274-36cc-be48-307917ff67aa | -3.69188 | -60.57145 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2b78198-6cf3-3fb9-ac35-4289f6d181fc | -3.34824 | -59.8491 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d92bd022-6a4a-3676-a189-d926ca4575a8 | -3.4899 | -60.36983 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3797eb94-3f2d-380f-82e8-25cf9ed3ecf5 | -3.33823 | -59.44453 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31c80d96-76ff-3359-a042-1d3098a2c33d | -3.49202 | -59.57382 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bce52fe-24e9-3f76-83b5-51d8d5245280 | -3.78364 | -51.92503 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2e3a015-a03d-3254-90d2-ad0ec5941eec | -4.40431 | -55.23926 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ac09ca2-b800-33e1-b83d-ce6db6b40756 | -4.0728 | -52.12525 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ad67ab-4a47-3aa1-a66c-84fdd42e8099 | -4.35241 | -55.64364 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aa7cfc3-7190-3831-b6d7-cb87a95b0d3b | -3.45283 | -58.21315 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41869381-6774-3d38-a819-fb13d1182dd6 | -3.82478 | -58.89053 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b508237d-8e03-3c70-a17c-1bfafab5fcef | -3.06529 | -61.28208 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b1edce8-0d36-3d96-8c64-aaf181aaef4c | -3.89824 | -60.59236 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9edb5f71-01b7-325c-a171-02a3feed9fbd | -3.75129 | -58.32773 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b596ab4-905e-30fd-a7a2-f620156d6441 | -3.6891 | -60.58904 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32743f68-4877-3bb3-8994-8651251353be | -3.38456 | -61.2966 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e72a7c-3eb7-3e37-8cae-d7370b0c8906 | -3.06029 | -61.27068 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d821f4-76ba-31f6-90c2-2eb0ce0e5150 | -3.48227 | -59.59127 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb8e1e52-3e31-35ff-afb3-019de198beb7 | -4.35197 | -55.49842 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d58b20eb-af70-34b4-9d77-b27583d22852 | 1.21352 | -50.97953 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4b5c8aa-7ff0-3f96-ab33-da80aa9d388a | -3.07949 | -61.17104 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README88.md)
