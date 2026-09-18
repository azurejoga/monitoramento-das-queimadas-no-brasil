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
| 811c2cac-65f8-3434-8a2f-d2fca7d34835 | -8.44268 | -45.7065 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6366357-985a-3cec-bf53-afd97352162c | -4.94201 | -42.88723 | 2026-09-18 03:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cb735a53-8a40-3a82-bc30-d75b1784611a | -7.93958 | -44.81855 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1a272dc-33c9-3906-9f0e-33a010e1d102 | -7.13811 | -42.09063 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77536f21-88fc-30aa-9361-27979fa8e3dd | -7.65933 | -46.10239 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7199b8e-a20b-3fd5-826e-4056cc675fa6 | -6.91064 | -41.72085 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0e13fbc-8a30-3886-aaa7-e6f5246fc02a | -6.30325 | -41.77984 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 336a607e-db29-393b-a4bf-57301c0f316c | -7.33884 | -44.62708 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ef5fab-0f52-363a-8742-e12a0adfbdc5 | -7.20051 | -44.11022 | 2026-09-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46b01221-aed3-3aa9-91a3-7392618e8200 | -5.62916 | -40.86443 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b980a7f-f0f8-34f4-b040-0ac1cf867574 | -4.5695 | -42.96231 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d58b6a05-06ad-3684-a0a2-b2abfcfa77ca | -6.28838 | -41.79976 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1e3d95e-710c-322a-b40f-cd17b596db8e | -7.19432 | -41.80777 | 2026-09-18 03:36:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1511c2c-d9b2-3b06-9ac0-73f976f26dc4 | -4.55791 | -42.95334 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a124a46-329a-348d-a338-1021d531ec51 | -8.45648 | -44.50535 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e326a2-4284-3187-8f6d-a622ef743a84 | -4.13871 | -44.25537 | 2026-09-18 03:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24f3ade1-ff6a-3bdf-99fb-57c0d1c339a8 | -5.62264 | -40.87112 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f2c5a63-86f7-3960-91e4-e0848d365628 | -7.93468 | -44.84361 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e2996a4-7a33-36e1-a1a4-6f8c76775a1b | -7.00954 | -43.63872 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 48f0afc9-88f2-3f45-95e9-87208ae1cdfb | -8.70255 | -44.88974 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e3ea8de-48a9-34b8-a06e-72dcc9de1a33 | -8.71191 | -44.88165 | 2026-09-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2558415-d377-3ca9-b712-d834fb84b918 | -8.90711 | -45.01181 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 061e24a6-ca13-37e5-86c1-f8062866e125 | -8.90659 | -45.01807 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 56c7c067-3164-35df-a8eb-883df838c941 | -5.75898 | -45.09393 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8a2e2b0-41e2-32ae-b346-60dd740dc786 | -4.58767 | -42.96576 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6dc9ef1f-c16c-3631-8b87-6116edce0015 | -7.05469 | -46.22419 | 2026-09-18 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8e93dc0a-9329-3a5e-ba92-724932c121f7 | -8.55295 | -44.90253 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 593aeee7-bef4-3354-9c8a-cda1c9f8716b | -4.55107 | -42.95675 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33f995f7-160a-3790-8108-dc694afe4637 | -4.55946 | -42.94425 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 809e01f3-8e28-33ed-b12c-b6d97bf03dba | -7.34999 | -44.63877 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d4d8614-fafe-38b3-b183-188e08f61f37 | -6.45549 | -46.01262 | 2026-09-18 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68b4bb0b-158d-3b69-8e87-1ca28301ac7d | -5.04787 | -42.61826 | 2026-09-18 03:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 021a98d5-06d9-3dc7-94b8-977447fb08b7 | -7.00242 | -43.64415 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2bb7d99e-d50e-377f-8380-7b10cbcb97e6 | -6.96232 | -42.56857 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94c9b91c-5e77-369e-bf97-866fd3b69e35 | -4.55215 | -42.95424 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d2de6c1-b051-3231-8efb-06546f4c30a1 | -6.91596 | -41.7222 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ded6aba-403e-37ea-8bb0-b048614f2557 | -4.55028 | -42.96135 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42022d77-1277-337b-93c0-2815a6362271 | -6.90997 | -41.71373 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d59c1937-106d-3e74-8e5d-eb797d56b5fe | -8.44136 | -45.71321 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ec1e977e-aa61-3060-9b91-2013a022493a | -7.00468 | -43.87017 | 2026-09-18 03:36:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8fa0652b-bb32-3bde-b010-de7ce757cd22 | -7.29052 | -38.96042 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 05f8cf4e-c4a1-3ad0-a221-ab8053bbe75b | -4.56317 | -42.95917 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c49ab607-728f-3173-94eb-de6b9b284411 | -7.34533 | -44.62795 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4e42314-8255-385c-9f7d-36cc07b50d64 | -5.75217 | -45.09286 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ca20e028-af10-3746-b909-2b253fb7c7b0 | -4.55869 | -42.9488 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd2dccea-7f7f-3c6f-9f2a-798175048139 | -4.93597 | -42.88633 | 2026-09-18 03:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb8cfc53-1c99-3c66-bd74-e3795d4ed8ea | -5.75102 | -45.09897 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 36869331-c5d6-351a-be48-bfc9d60ac2ca | -7.66182 | -46.08955 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc25ba4f-2a99-336a-9b19-500e75f0c1db | -5.61914 | -40.86037 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c6d202ec-7062-38cb-a656-372cda747fc8 | -5.63273 | -44.81163 | 2026-09-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eade17b0-3a90-3fb3-81cd-1dfa0c6cd6a0 | -5.72967 | -43.28299 | 2026-09-18 03:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8de8eaaf-ca7a-34ea-9e69-ff8dc18151e0 | -5.62325 | -40.86763 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e30b7cc-c326-3e11-badc-0df4e79d3d99 | -7.33232 | -44.62635 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7dc64c1-bcb0-3fa8-9909-4e8734a325d1 | -8.44522 | -45.83612 | 2026-09-18 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce2acf42-a001-37f0-8f7c-36d689ec6597 | -6.29451 | -41.79708 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c41c127-e98a-3b21-bb79-1092bb1002ed | -7.79569 | -44.90461 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 215a795e-c669-3de2-af73-350655c79993 | -7.0181 | -43.62766 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0257b2b-db2b-3eb2-94d2-15b1e7961ef8 | -5.75651 | -45.09781 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a86bcbcd-d4a9-312b-8c91-31e13bbff9c2 | -6.29517 | -41.79344 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d92bfa6-2226-31dd-8027-6e590277748b | -7.80328 | -44.90005 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d411a847-e2ee-3864-91f1-c7082e368c76 | -6.29711 | -41.78257 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0185b140-2998-316a-a12b-b0051b66d84f | -7.36335 | -44.46918 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bb5dadd-9e81-321c-97b4-f31e28d1b1a0 | -4.55902 | -42.95085 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3363671e-0d3d-39ec-879f-44bb3af53e08 | -7.00557 | -43.8654 | 2026-09-18 03:36:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 14625163-a644-3af2-a1cb-3f48514f46d4 | -7.79678 | -44.89889 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d1150ac-62d9-3476-a6ad-a8b1539538fa | -8.6785 | -45.43576 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3b43b27-b546-3393-a4fb-cc0b3a058562 | -4.56507 | -42.95197 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ddba323-7cef-3ac5-a3cd-b1a5c95c20e3 | -8.68241 | -45.439 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ef4a1ea-08b1-3174-be34-c32e523c153e | -7.34967 | -38.98938 | 2026-09-18 03:36:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dcab3582-3c96-37d7-b441-25c632e7f347 | -6.61377 | -44.20895 | 2026-09-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e2615e3-160f-39fd-b01f-fd5f04da579b | -7.81417 | -44.91361 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74b15874-6520-3194-be8b-04128c1c56ce | -6.60734 | -44.20829 | 2026-09-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8912f4f3-897f-3caa-8d6c-906e7c2b9714 | -6.66241 | -43.63866 | 2026-09-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd20b3a-e4aa-351c-801a-93549ef3f0b7 | -8.46138 | -44.52982 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 771800a1-97ad-3023-bb0a-5ace2c65201a | -5.32771 | -45.15032 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fae7c2f-7ac1-313a-83af-889549870efe | -8.45891 | -44.50821 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fda3614e-b02c-3972-b513-192a10a7606e | -4.85098 | -43.54942 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b5ecace7-4119-3989-b2c0-0ffd009fc24e | -7.01636 | -43.63699 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 653cca51-13e2-34a5-9157-aad319e4fd85 | -7.19427 | -44.10902 | 2026-09-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e35a8658-1ef8-3a1e-8233-c0970f66f43f | -7.01114 | -43.63124 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8dfd121-f694-39dd-b68a-f28c63791c54 | -6.28773 | -41.80336 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e1031cc-1c9d-3c27-95c7-472cb54dddd2 | -8.93982 | -44.39606 | 2026-09-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c44270c-6ca8-38f0-abb0-2d531dbd2ff1 | -6.61473 | -44.20377 | 2026-09-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 838dd27b-1e8c-3601-b978-bb2e0803d4c2 | -6.30259 | -41.78349 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbc5ddfd-457d-3622-80cf-2b4afa22e19d | -6.4094 | -43.4669 | 2026-09-18 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b197b691-04ce-328c-8153-027c8725e671 | -4.40436 | -42.31421 | 2026-09-18 03:36:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a0d92cb-9af5-3fb0-83e9-d291997c595c | -7.00344 | -43.63765 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ac1ddd29-fc09-3afb-a80a-f4c1527aa730 | -5.75536 | -45.10415 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 74920d1b-5fc8-3cd4-9521-ae78a9b8b147 | -7.67446 | -46.09887 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 224f9c1a-d856-3736-93c6-6c413b751976 | -7.04412 | -42.07798 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77f95bfc-d74b-3c4e-8b69-12f1fcb715cc | -4.57033 | -42.95764 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0fc3e83b-a5b6-3e0e-ab35-a1865ee04179 | -7.7925 | -44.88599 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb8810d5-b0c9-390b-baff-c29caba95aa8 | -8.70992 | -44.88578 | 2026-09-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d233502-6cda-30a4-bc1a-9ea6b0cf771f | -7.6606 | -46.09583 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bee66315-f8d9-338d-841a-e6bca72869ef | -4.56474 | -42.94997 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20f349cb-0909-3812-9ab7-f057305b569f | -8.90028 | -45.01626 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3455ff0f-57c2-30d1-833d-e4fd55b53ec8 | -6.66323 | -43.63412 | 2026-09-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bfd8e4-9c1c-3b24-9962-985ebb9aeeef | -7.67317 | -46.10559 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 702e2e3b-002e-39e0-955e-761b84c73b2e | -5.61858 | -40.86359 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8f02733-3341-3a5c-b2a5-877500f72b83 | -7.01027 | -43.63588 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README25.md)
